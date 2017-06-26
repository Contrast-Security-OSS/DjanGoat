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
        if 'HTTP_REFERER' in request.META:
            referrer = request.META['HTTP_REFERER']
        else:
            referrer = ""

        if 'HTTP_USER_AGENT' in request.META:
            user_agent = request.META['HTTP_USER_AGENT']
        else:
            user_agent = ""

        Analytics.objects.create(ip_address=self.get_client_ip(request),
                                 referrer=referrer,
                                 user_agent=user_agent,
                                 created_at=pytz.utc.localize(
                                     datetime.datetime.now()),
                                 updated_at=pytz.utc.localize(
                                     datetime.datetime.now()))
        return None
