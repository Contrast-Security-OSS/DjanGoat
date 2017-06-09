from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Benefits(models.Model):
    """
        Benefits Model which includes the file upload and save logic for the
        path traversal rule.
    """
    def __str__(self):
        return "Benefits " + str(self.created_at)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
