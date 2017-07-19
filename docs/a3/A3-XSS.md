# A3: Cross Site Scripting XSS

### Description

This vulnerability occurs when user input is sent to a browser without validation or escaping, thus allowing scripts to be executed in user browsers.
The following code was taken from template/layouts/shared/nav_loggedin.html:
```
<li class="nav-item">
    <a class="nav-link" href="#">Welcome, {{ current_user.safe_name }}</a>
</li>
```

where current_user.safe_name can be found in app/models/User/user.py.

```

def safe_name(self):
    return mark_safe(self.first_name)
```

### Why would someone do this?

Many developers use mark_safe to bypass the issue of funny characters displaying, and as a workaround for issues with jquery.
Any situation in which a developer would want to render HTML code in literal form could potentially lead to this vulnerability.
The fact that safe is in the name of this function, which in fact makes a string unsafe, can be deceiving.

### Attack

Go to the sign up page and enter your first name as some javascript, for example one of the following:
```
<script>document.write("<b>dog</b>")</script>
```
```
script>alert(1)</script>
```
```
<form action="/action_page.php">First name:<br><input type="text" name="firstname" value="cat"><br>Last name:<br><input type="text" name="lastname" value="dog"><br><br><input type="submit" value="Submit"></form>
```
When you sign up with the new user, the header bar will echo "Welcome" + your code. Each new page you navigate to while logged in as that user should execute that code.

### Solution

For this example, simply displaying first_name instead of safe_name would eliminate the attack because Django has built in defense against XSS attacks and will autoescape. If you wanted to render HTML code in literal form, you could use something such as format_html().