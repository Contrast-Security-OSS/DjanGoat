# A6 Sensitive Data Exposure: Cleartext Storage and Transmission of SSNs

### Description of bugs
Social Security Numbers, part of the WorkInfo model, are not stored or transmitted securely in the application. These bugs are as follows: 

1. SSN is not encrypted before being stored in the database
2. The full, unencrypted SSN is sent back in an HttpResponse object. It is only obscured with asterisks client side using javascript

If a malicious user gained access to the database, he or she would be able to clearly see all users' SSNs. Multiple layers of protection are important. Additionally, whenever a WorkInfo model is retrieved from the database and sent to the user, there is potential for access that should not be allowed. There is very little point in obscuring the SSN with javascript client-side because the user can easily reverse this.

### Why would someone do this?
It is important to think how the data can be accessed at every point of the application, whether in the database, traveling from the database to the client, or just at the client side. 
While there really is no excuse for having cleartext storage of sensitive data in your database, according to the OWASP Top 10, this is the most common instance of this vulnerability. 

However, a smart django developer could mistakenly beleive the sensitive data is secure if the data is encrypted in the database and shown obscured in the view. 
But transferring data over the internet is extremely dangerous, as it can be easily intercepted. 
The data should be passed as encrypted or at least partially encrypted so the user can decide whether or not they are in a safe enough place to access the sensitive data.

### Solution
In order to fix these bugs, you must

1. Force the SSN to be stored as an encrypted value in the database.
2. Only pass the last four digits of the unencrypted SSN to the view from the model. 

#### 1. Force the SSN to be stored as an encrypted value in the database.
Since multiple models have sensitive data, we included an encryption class in a common file called utils.py in the 'app/models' directory. The most important functions in this class are encrypt_sensitive_value and decrypt_sensitive_value, shown below:
```python
class Encryption():
 
    @staticmethod
    def encrypt_sensitive_value(user, value):
        aes = AES.new(Encryption.get_key(), AES.MODE_CBC, Encryption.get_iv(user))
        return aes.encrypt(Encryption.pad(value))
 
    @staticmethod
    def decrypt_sensitive_value(user, value):
        aes = AES.new(Encryption.get_key(), AES.MODE_CBC, Encryption.get_iv(user))
        return Encryption.unpad(aes.decrypt(value))
```
These functions are already implemented to encrypt and decrypt SSN, but they are not currently used. These functions are called encrypt_ssn and decrypt_ssn respectively, and can be found in /app/models/WorkInfo/work_info.py 

In order to make the SSN be encrypted, you must create a signal to run the encrypt_ssn method whenever the WorkInfo model is created. This can be done in the app/signals.py file. This should look like:
```python
from app.models import WorkInfo
 
 
@receiver(pre_save, sender=WorkInfo)
def encrypt_ssn(sender, instance, *args, **kwargs):
    if instance.pk is None:
        instance.encrypt_ssn()
```
This function runs every time the save method is run on an instance of a WorkInfo object, but by checking that the primary key is none, encrypt_ssn() only runs before the WorkInfo object is put in the database. 

#### 2. Only pass the last four digits of the unencrypted SSN to the view from the model. 
To do this, first delete the javascript that obscures the first 5 digits of the SSN located in /template/users/work_info/index.html. This javascript is located at the bottom of the page, lines 44 to 51. Now, if you refresh the page, the whole SSN should be shown. 

Next, add a method on the WorkInfo model called last_four_of_ssn, which returns a string representation of the SSN associated with the workinfo, with the first 5 digits replaced with asterisks. Here's an example of what this would look like:
```python
def last_four_of_ssn(self):
    return "***-**-" + self.decrypt_ssn()[-4:]
```

To show the last four digits of the ssn, simply edit the table that displays the work info data. Specificially, change the line where SSN is accessed, because now it will show the encrypted value of the ssn. The resulting html is shown below:


```html
<tr>
    <td>{{ current_user.full_name }}</td>
    <td>{{ work_info.income }}</td>
    <td>{{ work_info.bonuses }}</td>
    <td>{{ work_info.years_worked }}</td>
    <td class="ssn">{{ work_info.last_four_of_ssn() }}</td>
    <td>{{ work_info.DoB }}</td>
</tr>
```
Congrats! Now your WorkInfo view and model are secured against sensitive data exposure due to cleartext storage.



