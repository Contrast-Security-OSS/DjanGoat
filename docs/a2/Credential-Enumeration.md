# A2: Credential Enumeration

### Description

This vulnerability comes from app/views/session/views.py
```python
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

This provides overly verbose error messages that indicate whether or not a user exists. An attacker can guess password for existing accounts.
### Attack

At login page, using not registered email to login gives 'Email incorrect!' message; using registered email and wrong password to login gives 'Password incorrect!' message.