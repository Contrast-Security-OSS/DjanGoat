# A2: Credential Enumeration

### Description

This vulnerability occurs when an application is overly verbose about error messages. Messages that indicate whether a user exists or not can help attacker to guess password for existing accounts.

The vulnerability comes from app/views/session/views.py
```
try:
    response = HttpResponseRedirect(path)
    user = User.authenticate(email, password)
    response.set_cookie("auth_token", user.auth_token)
    return response
except User.DoesNotExist:
    message = "Email incorrect!"
except Exception as error:
    if u'Incorrect Password' in error.message:
        message = "Password incorrect!"
    else:
        message = str(error)
messages.add_message(request, messages.INFO, message)
```


### Why would someone do this?

It is a good practice to be verbose when writing and testing applications. Developer can use such verbose message to test whether or not the application behavior is what they expect.

However, leaving such verbose message can also hand over information to attackers.

### Attack

At login page, using not registered email to login gives 'Email incorrect!' message; using registered email and wrong password to login gives 'Password incorrect!' message.

### Solution

Display the same message when login fails.
```
try:
    response = HttpResponseRedirect(path)
    user = User.authenticate(email, password)
    response.set_cookie("auth_token", user.auth_token)
    return response
except User.DoesNotExist:
    message = "Email or Password incorrect!"
except Exception as error:
    if u'Incorrect Password' in error.message:
        message = "Email or Password incorrect!"
    else:
        message = "Something went wrong"
messages.add_message(request, messages.INFO, message)
```