# A3: DOM-Based Cross Site Scripting XSS

### Description

Consider a situation in which the DOM "environment" can be modified, such as which language to display a website in.

The following code was taken from template/users/signup.html:
```
<!-- support for multiple languages coming soon! -->
<script>
    //document.write("<select style=\"width: 100px;\">");
    //document.write("<OPTION value=1>English</OPTION>");
    //document.write("<OPTION value=2>Spanish</OPTION>");
      var hashParam = location.hash.split("#")[1];
      var paramName = hashParam.split('=')[0];
      var paramValue = decodeURIComponent(hashParam.split('=')[1]);
      document.write("<OPTION value=3>" + paramValue + "</OPTION>");
    //document.write("</select>");
</script>
```
It takes user input (params), and renders it back on the page without any output encoding or escaping.

### Attack

This has to be done in Firefox. Use the following link (substitute hostname for your actual hostname) to execute an alert box:
http://127.0.0.1:8000/signup/#test=<script>alert(1)</script>
You can replace the script with whatever you want to try.

### Solution

Make sure to properly escape user input. This can be done by writing a function that replaces common characters in script such as the less than or greater than signs.