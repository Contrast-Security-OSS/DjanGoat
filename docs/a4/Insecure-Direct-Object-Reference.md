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

The error is present in line 12. Rather than get the user_id based off the authentication used by the application, this method looks up the user by the parameter from the url, allowing the user to view any WorkInfo page.