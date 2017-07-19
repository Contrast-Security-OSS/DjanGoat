**Description:**
 When a user is accessing the api endpoint, via a GET request to api/v1/users or to api/v1/users/(user_id)
 the returned json data contains sensitive data including password information and authorization tokens.
 Authorization tokens are improperly validated.

**Why:**
Many applications that have an api use a token based system for api access.
Validation is commonly done through regular expressions and string manipulation.
Problems arise when these validation methods are not rigorously tested.

**Attack:**

**Part 1:** Sensitive Data Exposure
Go ahead to app/views/api/users/views and look at the view function api_index.
Comment out the if statement check for a valid api token and simply return the HttpResponse containing the serialized data.
Your code may like this:
```python
@require_http_methods(["GET"])
def api_index(request):
     # if check_if_valid_token(request):
     #    try:
     #        token = urlparse.unquote(request.META['HTTP_AUTHORIZATION'])
     #        user_id = extrapolate_user(token)
     #        user = User.objects.get(user_id=user_id)
     #        if user.is_admin:
     #            data = serializers.serialize("json", User.objects.all())
     #            return HttpResponse(data, content_type='application/json')
     #        else:
     #           data = serializers.serialize("json", User.objects.filter(user_id=user_id))
     #            return HttpResponse(data, content_type='application/json')
     #    except User.DoesNotExist:
     #        return HttpResponse("null", content_type='application/json')
     # else:
     #    return HttpResponse('Unauthorized', status=401)
      data = serializers.serialize("json", User.objects.all())
      return HttpResponse(data, content_type='application/json')
```
Now when you start your application and go to localhost:8000/api/v1/users you can see all of the users in your database including their password information.

**Part 2:** Api Token Generation
 Go ahead and revert the code to how it originally looked. Now when you access either of the routes you'll get a 401!
 To fix this you'll need to add an additional header to your request.
 Capture the request to the api and open it up in some sort of proxy.
  Then add a header called authorization and add a token as found in the credentials section of the tutorial

  ex) Authorization: Token token=2-050ddd40584978fe9e82840b8b95abb98e4786dc

 Hit send and you should see the insecure data again!

**Part 3:** Tricking the API Token System

Failure to properly deal with url encoded characters can lead to significant vulnerabilities.
Let's begin by running through the how api system works.
We get a token like 2-050ddd40584978fe9e82840b8b95abb98e4786dc and we split into two groups - ['2', '050ddd40584978fe9e82840b8b95abb98e4786dc'].
We then check to make sure our token hash matches the encryption digest.
When we pass the check_if_valid_token test we go ahead and extrapolate the user in a separate function!
After all, we just verified that we have a clean token.
Moreover, since we do not want to deal with errors from accidental whitespace or newlines we'll just clean the token and take that first integer value. Then we take that user and make the query.

Let's use some trickery to around this system. Modify your request such that for the Authorization header you pass 'Token token=1%0a2-050ddd40584978fe9e82840b8b95abb98e4786dc'
Sent that request to api/v1/users and look what happens! The request returned all the data, even though user 2 is not an admin. With this trickery one can act like any other user and get the information of that user.

**Solution:**

Be sure to rigorously test your regular expressions as well as anchor them! Ensure you can handle all encoded content.
