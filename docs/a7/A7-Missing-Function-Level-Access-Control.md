**Description:** Administrative routes may not be properly safeguarded thus
                allowing unauthorized users to have admin level functionality

**Why:** There is no real reason why someone would allow a non admin to access admin functionality.

**Attack:**

```

@require_http_methods(["GET"])
@user_is_authenticated
def admin_dashboard(request, selected_id):
    current_user = utils.current_user(request)
    return render(request, 'admin/dashboard.html', { 'current_user': current_user})

```
Note how there are no restrictions at all to get to the admin dashboard besides just logging in as one.
Try logging in as a normal user. Then change your url to admin/1/dashboard. You are now an admin!.


**Solution:**

Add an additional filter that checks whether the requested user is an admin. You could take advantage
of the user's cookies to make this authentication. You could then redirect the user back to he or she's current page