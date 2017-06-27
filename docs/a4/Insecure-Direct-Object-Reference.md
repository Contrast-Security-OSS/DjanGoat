# A4: Insecure Direct Object Reference

### Description of bugs
The WorkInfo Page is not protected against Direct Object Reference. This means that an authenticated user can access any other user's WorkInfo page simply by trying different ids in the url. For example, if a malicious user had an id of 5, his WorkInfo page would be "pygoat/users/5/work_info". It isn't hard to guess that other user's would follow the same pattern. By allowing access to the WorkInfo page without proper authorization, other user's are open to attacks and identity theft. 

This is allowed due to the way the current user is retrieved in the user_work_info_index method in "app/views/users/work_info/views.py", shown below.
```python
@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_work_info_index(request, user_id):
    user = User.objects.get(id=user_id)
    work_info = user.work_info.first()
    context = {'current_user': user,
               'work_info': work_info}
    return render(request, "users/work_info/index.html", context=context)
```

The error is present in third line of code. Rather than get the user_id based off the authentication used by the application, this method looks up the user by the parameter from the url, allowing the user to view any WorkInfo page.

### Why would someone do this?
While in our example, this is a clear case of bad programming practices, oftentimes bugs like these are caused by good ideas. Since authentication is already required to access this method based on the decorator, a django developer might presume themselves to be "safe" once they are inside it. The reality is, just because someone is authenticated does not mean they are not potentially malicious. 

Additionally, simply querying the database for all objects with an attribute matching a parameter of the function is much less resource-intensive than essentially re-doing authentication to make sure the parameter is valid for the current user.

### Solution
In order to fix these bugs, you must replace the line of code in line 12 to retrieve the current user based on the application's authentication system. In the case of pygoat, we store an auth_token stored locally as a cookie to manage a user's session. By retrieving the locally stored and unique authorization token from the user, we can lookup the user in the database. Luckily, we have already implemented a method that does this, as WorkInfo is not the only page that should only be able to display the current user's information. The method is in "app/views/utils.py", shown below.

```python
def current_user(request):
    return User.authenticate_by_token(request.COOKIES['auth_token'])
```
So, to fix the insecure direct object reference in WorkInfo, simply import this module into views.py and use the current user method rather than a database query based on the user_id parameter. This implementation is shown below:

```python
from app.views import utils
 
 
@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_work_info_index(request, user_id):
    user = utils.current_user(request)
    # Do the rest of the method the same way
```

Congrats! Now your WorkInfo view is now secured against insecure direct object reference. 
