import pep8


# Mixin for testing the pep8 style rules
class Pep8ViewsTests(object):

    def test_pep8_conformance_views(self):
        file_path = self.path + 'views.py'
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([file_path])
        error_message = ""
        if result.total_errors != 0:
            error_message = "Style errors in: " + file_path + "\n" + "\n".join(result.get_statistics())
        self.assertEqual(result.total_errors, 0, error_message)

    def test_pep8_conformance_urls(self):
        file_path = self.path + 'urls.py'
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([file_path])
        error_message = ""
        if result.total_errors != 0:
            error_message = "Style errors in: " + file_path + "\n" + "\n".join(result.get_statistics())
        self.assertEqual(result.total_errors, 0, error_message)

    def test_pep8_conformance_init(self):
        file_path = self.path + '__init__.py'
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([file_path])
        error_message = ""
        if result.total_errors != 0:
            error_message = "Style errors in: " + file_path + "\n" + "\n".join(result.get_statistics())
        self.assertEqual(result.total_errors, 0, error_message)