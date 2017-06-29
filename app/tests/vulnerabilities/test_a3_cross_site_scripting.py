from __future__ import unicode_literals
from django_webtest import WebTest


class CrossSiteScriptingTest(WebTest):
    def setUp(self):
        self.param = {'email': 'catdog@gmail.com',
                      'last_name': 'dog', 'password': '123456',
                      'confirm': '123456'}
        page = self.app.get('/signup/')
        form = page.forms[0]
        form.set('email', self.param['email'])
        form.set('last_name', self.param['last_name'])
        form.set('password', self.param['password'])
        form.set('confirm', self.param['confirm'])
        self.form = form

    # the first name field is where the vulnerability occurs, so by testing how
    # many forms are on the dashboard page with different first names, we can
    # confirm that the xss attack has executed correctly
    def test_header_xss_0_forms(self):
        first_name = 'dogs'
        self.form.set('first_name', first_name)
        self.form.submit()
        page = self.app.get('/dashboard/home')
        self.assertEqual(len(page.forms), 0)

    def test_header_xss_1_form(self):
        first_name = '<form action="/action_page.php">First name:<br><input type="text" name="firstname" value="dog"><br><br><input type="submit" value="Submit"></form>'
        self.form.set('first_name', first_name)
        self.form.submit()
        page = self.app.get('/dashboard/home')
        self.assertEqual(len(page.forms), 1)

    def test_header_xss_2_forms(self):
        first_name = '<form>dogs</form><form>cat</form>'
        self.form.set('first_name', first_name)
        self.form.submit()
        page = self.app.get('/dashboard/home')
        self.assertEqual(len(page.forms), 2)

    def test_header_xss_3_forms(self):
        first_name = '<form>dogs</form><form>cat</form><form>bird</form>'
        self.form.set('first_name', first_name)
        self.form.submit()
        page = self.app.get('/dashboard/home')
        self.assertEqual(len(page.forms), 3)
