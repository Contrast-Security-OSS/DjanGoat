# A1: SQL Injection Interpolation

### Description

This vulnerability occurs when the application interpolates user-provided input into SQL queries. An attacker can send text-based attacks that exploit the targeted interpreter. Such injection can result in data corruption or denial of access.

The vulnerability can be found at app/models/Analytics/analytics.py
```
@classmethod
def hits_by_ip(cls, ip, col='*'):
    table_name = cls.objects.model._meta.db_table
    cmd = "SELECT %s FROM %s WHERE ip_address='%s' ORDER BY id DESC" % (
        col, table_name, ip)
    with connection.cursor() as cursor:
        cursor.execute(cmd)
        raw = cursor.fetchall()
    formated = Analytics.format_raw_sql(cmd, raw)
    return formated
```

The command that application executes directly uses the col parameter from user, which can be varied by url.

### Why would someone do this?

Developers want to select columns directly from the database using SQL commands to achieve the functionality at analytics page. The url for column selection is automatically generated, so developers could assume that user will not change the data.

However, it is always a good practice to pre-process values that users have control over.

### Attack

After login, on page http://127.0.0.1:8000/admin/1/analytics, you should be able to see a table of information about analytics.

However, using urls like http://127.0.0.1:8000/admin/1/analytics?ip=127.0.0.1&email=&password%20FROM%20app_user%3B%20select%20user_agent= will grant you access to all user email and password. By injecting SQL commands at url, attackers can take control over any column in the database.

### Solution

1. Using a white list of columns to pre-process the input, then pass the result to query command.
    ```
    @staticmethod
    def parse_field(field):
        valid_fields = ["ip_address", "referrer", "user_agent"]
        if field in valid_fields:
            return field
        else:
            return '1'
    ```
2. Use Django builtin QuerySet API to select the values from database.