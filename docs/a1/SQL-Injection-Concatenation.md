# A1: SQL Injection Concatenation

### Description

This vulnerability occurs when untrusted data is sent to an interpreter as part of a command or query. Unintended commands may be executed to grant attacker access to unauthorize data.

The vulnerability can be found at app/views/users/views.py
```
@require_http_methods(["GET", "POST", "PUT", "DELETE"])
@user_is_authenticated
def user_view(request, user_id):
    if request.method == "POST":
        form = request.POST
        if not form:
            return HttpResponse("User " + str(user_id) + "POST")
        user_id_form = form['user_id']
        table_name = User.objects.model._meta.db_table
        # The order by is_admin='0' moves admin to the first in list
        # which allows sql injection
        users = User.objects.raw(
            "SELECT * FROM %s WHERE user_id='%s' ORDER BY is_admin='0'"
            % (table_name, user_id_form))
```

The code is directly using form data to execute SQL command. An attacker can change the form to have access to some queries and update their information.

### Why would someone do this?

In order to find the current user and update his information, developers want to get the ID of the current user somewhere, so they store the information at a hidden field in form. This is not a good practice because the hidden field can be changed by an attacker.

### Attack

This is one way of doing a command injection:
1. Set up an intercepting proxy
2. Login and navigate to account settings page
3. Fill the form and submit
4. Intercept the POST request, which should look like:
    ```
    csrfmiddlewaretoken=GH8SDbVSwfmxi48PtglTK5i8j9QAIw1IqlWQ9NOLvhTcAe7gDGODqx59qqJvrKK4&user_id=1&email=&first_name=&last_name=&password=&confirm=
    ```
5. Execute a SQL injection as below and resend the request:
    ```
    csrfmiddlewaretoken=GH8SDbVSwfmxi48PtglTK5i8j9QAIw1IqlWQ9NOLvhTcAe7gDGODqx59qqJvrKK4&user_id=1' OR is_admin = '1&email=&first_name=&last_name=&password=123456&confirm=123456
    ```
6. This injection changes the first found admin's password to 123456 

### Solution

Instead of using user ID from form to find the current user, we can directly get the current user from the current session.
```
from app.views import utils
user = utils.current_user(request)
```
