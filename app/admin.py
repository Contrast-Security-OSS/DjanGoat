# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Note
from models import Benefits
from models import User
from models import PaidTimeOff
from models import KeyManagement
from models import Pay
from models import Performance
from models import Retirement
from models import Schedule
from models import WorkInfo

# Register your models here.
admin.site.register(Note)
admin.site.register(User)
admin.site.register(PaidTimeOff)
admin.site.register(KeyManagement)
admin.site.register(Pay)
admin.site.register(Performance)
admin.site.register(Retirement)
admin.site.register(Schedule)
admin.site.register(WorkInfo)
admin.site.register(Benefits)
