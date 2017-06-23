from app.models import Analytics
import pytz
import datetime


class AnalyticsStorageMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def process_request(self, request):
        Analytics.objects.create(ip_address=self.get_client_ip(request),
                                 referrer=request.META['HTTP_REFERER'],
                                 user_agent=request.META['HTTP_USER_AGENT'],
                                 created_at=pytz.utc.localize(
                                     datetime.datetime.now()),
                                 updated_at=pytz.utc.localize(
                                     datetime.datetime.now()))
        return
