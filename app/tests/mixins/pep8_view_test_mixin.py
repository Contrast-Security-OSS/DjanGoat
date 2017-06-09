import pep8


# Mixin for testing the pep8 style rules.
class Pep8ViewsTests(object):

    def test_pep8_conformance_views(self):
        file_path = self.path + 'views.py'
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([file_path])
        self._validate(result, file_path)

    def test_pep8_conformance_urls(self):
        file_path = self.path + 'urls.py'
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([file_path])
        self._validate(result, file_path)

    def test_pep8_conformance_init(self):
        file_path = self.path + '__init__.py'
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([file_path])
        self._validate(result, file_path)

    # Helper method to validate whether or not there are pep8 errors in the code specified by the path
    def _validate(self, result, path):
        error_message = ""
        if result.total_errors != 0:
            error_message = "Style errors in: " + path + "\n" + "\n".join(result.get_statistics())
        self.assertEqual(result.total_errors, 0, error_message)
