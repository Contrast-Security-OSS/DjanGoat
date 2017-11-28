# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from app.models import Note
from app.models import Analytics
from app.models import Benefits
from app.models import User
from app.models import PaidTimeOff
from app.models import KeyManagement
from app.models import Pay
from app.models import Performance
from app.models import Retirement
from app.models import Schedule
from app.models import WorkInfo

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
admin.site.register(Analytics)
admin.site.register(Benefits)
