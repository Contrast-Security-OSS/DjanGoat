# A3: DOM-Based Cross Site Scripting XSS

### Description

Consider a situation in which the DOM "environment" can be modified.

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

### Why would someone do this?

In this specific example, the vulnerability lies in a half-developed feature in which the language option is parsed from the url.
Following that, it is easy to imagine many situations in which a developer may want to allow for modification of the DOM environment.
Such modifications can easily lead to XSS vulnerabilities, as demonstrated in this example.

### Attack

This has to be done in Firefox. Use the following link (substitute hostname for your actual hostname) to execute an alert box:
http://127.0.0.1:8000/signup/#test=<script>alert(1)</script>
You can replace the script with whatever you want to try.

### Solution

Make sure to properly escape user input before rendering it back on the page. This can be done by writing a simple function that replaces common characters in script such as the less than or greater than signs.