from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
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

    # uploaded_file expects to be a UploadedFile object from request.FILES
    # in Django
    # this way of saving data leaves intended vulnerability
    @staticmethod
    def save_data(uploaded_file, backup=None):
        data_path = os.path.join(settings.MEDIA_ROOT, "data")
        full_file_name = os.path.join(data_path, uploaded_file.name)
        # the uploaded file is read at once, as duplicated in railsgoat
        # use file.chunk() in a loop can prevent overwhelming system memory
        content = ContentFile(uploaded_file.read())
        default_storage.save(full_file_name, content)
        # using string "true" is intended to duplicate railsgoat's behavior
        if backup == "true":
            return Benefits.make_backup(uploaded_file, data_path,
                                        full_file_name)

    def silence_streams(func):
        def wrapper(*args, **kwargs):
            # save stderr
            save_streams = sys.__stderr__
            save_streams.flush()
            # file descriptor for stderr is 2
            save_stderr = os.dup(2)
            # silence
            null_fd = os.open(os.devnull, os.O_RDWR)
            os.dup2(null_fd, 2)
            # uncomment the line to test if stderr is silenced
            # 1/0
            try:
                bak_file_path = func(*args, **kwargs)
                sys.stderr = save_streams
                os.dup2(save_stderr, 2)
                return bak_file_path
            except:
                sys.stderr = save_streams
                os.dup2(save_stderr, 2)
        return wrapper

    @staticmethod
    @silence_streams
    def make_backup(orig_file, data_path, full_file_name):
        if os.path.isfile(full_file_name):
            epoch_time = int(time.time())
            bak_file_path = "%s/bak%d_%s" % (data_path, epoch_time,
                                             orig_file.name)
            # intended vulnerability for command injection
            os.system("cp %s %s" % (full_file_name, bak_file_path))
            return bak_file_path
