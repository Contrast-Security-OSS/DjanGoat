from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.utils import timezone
import os
import sys
import time


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

    class Meta:
        db_table = "app_benefits"

    # file expects to be a UploadedFile object from request.FILES in Django
    # this way of saving data leaves intended vulnerability
    @staticmethod
    def save_data(file, backup=False):
        data_path = os.path.join(settings.MEDIA_ROOT, "data")
        full_file_name = os.path.join(data_path, file.name)
        # the uploaded file is read at once, as duplicated in railsgoat
        # use file.chunk() in a loop can prevent overwhelming system memory
        content = ContentFile(file.read())
        default_storage.save(full_file_name, content)
        # using string "true" is intended to duplicate railsgoat's behavior
        if backup == "true":
            Benefits.make_backup(file, data_path, full_file_name)

    def silence_streams(func):
        def wrapper(*args, **kwargs):
            # save stdout, stderr
            save_streams = sys.__stdout__, sys.__stderr__
            for steam in save_streams:
                steam.flush()
            save_stdout = os.dup(1)
            save_stderr = os.dup(2)
            # silence
            null_fd = os.open(os.devnull, os.O_RDWR)
            os.dup2(null_fd, 1)
            os.dup2(null_fd, 2)
            try:
                func(*args, **kwargs)
            finally:
                # restore stdout, stderr
                sys.stdout, sys.stderr = save_streams
                os.dup2(save_stdout, 1)
                os.dup2(save_stderr, 2)
        return wrapper

    @staticmethod
    @silence_streams
    def make_backup(file, data_path, full_file_name):
        if os.path.isfile(full_file_name):
            epoch_time = int(time.time())
            # intended vulnerability for command injection
            os.system("cp %s %s/bak%d_%s" %
                      (full_file_name, data_path,
                       epoch_time, file.name))
