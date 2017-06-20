from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from app.models import User
from django.core import serializers
from Crypto.Hash import SHA
from pygoat.settings import ACCESS_TOKEN_SALT
import re


@require_http_methods(["GET"])
def api_index(request):
    if check_if_valid_token(request):
        data = serializers.serialize("json", User.objects.all())
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponse('Unauthorized', status=401)


@require_http_methods(["GET"])
def api(request, id_number):
    if check_if_valid_token(request):
        try:
            data = serializers.serialize("json", User.objects.filter(user_id=id_number))
            return HttpResponse(data, content_type='application/json')
        except User.DoesNotExist:
            return HttpResponse("null", content_type='application/json')
    else:
        return HttpResponse('Unauthorized', status=401)


# This is purposely vulnerable see - https://github.com/OWASP/railsgoat/wiki/Extras:-Broken-Regular-Expression
def check_if_valid_token(request):
    if 'HTTP_AUTHORIZATION' not in request.META:
        return False
    else:
        token = request.META['HTTP_AUTHORIZATION']
        regex = re.compile("(.*?)-(.*)")
        regex_groups = regex.match(token)
        if regex_groups.group(1):
            id = regex_groups.group(1)[len(regex_groups.group(1)) - 1:len(regex_groups.group(1))]
        else:
            return False
        if regex_groups.group(2):
            hash = regex_groups.group(2)
        else:
            return False
        sha = SHA.new()
        sha.update(ACCESS_TOKEN_SALT + ":" + str(id))
        return hash == sha.hexdigest()
