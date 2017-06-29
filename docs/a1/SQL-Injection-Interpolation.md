# A1: SQL Injection Interpolation

### Description

This vulnerability can be found at app/models/Analytics/analytics.py
```python
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

The command we execute directly uses the col parameter from user, which can be varied by url.

### Attack

After login, on page http://127.0.0.1:8000/admin/1/analytics, you should be able to see a table of information about analytics.

However, using urls like http://127.0.0.1:8000/admin/1/analytics?ip=127.0.0.1&email=&password%20FROM%20app_user%3B%20select%20user_agent= will grant you access to any column in the database.