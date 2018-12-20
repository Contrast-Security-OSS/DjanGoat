from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from app.models import User
from pygoat.settings import ACCESS_TOKEN_SALT
from Crypto.Hash import SHA
import re
import urlparse


@require_http_methods(["GET"])
def api_index(request):
    if check_if_valid_token(request):
        try:
            token = urlparse.unquote(request.META['HTTP_AUTHORIZATION'])
            user_id = extrapolate_user(token)
            user = User.objects.get(user_id=user_id)
            if user.is_admin:
                data = serializers.serialize("json", User.objects.all())
                return HttpResponse(data, content_type='application/json')
            else:
                data = serializers.serialize("json", User.objects.filter(user_id=user_id))
                return HttpResponse(data, content_type='application/json')
        except User.DoesNotExist:
            return HttpResponse("null", content_type='application/json')
    else:
        return HttpResponse('Unauthorized', status=401)


@require_http_methods(["GET"])
def api(request, id_number):  # pylint: disable=unused-argument
    if check_if_valid_token(request):
        token = urlparse.unquote(request.META['HTTP_AUTHORIZATION'])
        user_id = extrapolate_user(token)
        data = serializers.serialize("json", User.objects.filter(user_id=user_id))
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponse('Unauthorized', status=401)


# This is purposely vulnerable see - https://github.com/OWASP/railsgoat/wiki/Extras:-Broken-Regular-Expression
def check_if_valid_token(request):
    if 'HTTP_AUTHORIZATION' not in request.META:
        return False
    else:
        token = urlparse.unquote(request.META['HTTP_AUTHORIZATION'])
        regex = re.compile("(.*?)-(.*)")
        split_token = token.split('=')[1]
        regex_groups = regex.search(split_token)
        if regex_groups.group(1):
            group_id = regex_groups.group(1)
        else:
            return False
        if regex_groups.group(2):
            group_hash = regex_groups.group(2)
        else:
            return False

    sha = SHA.new()
    sha.update(ACCESS_TOKEN_SALT + ":" + str(group_id))
    return group_hash == sha.hexdigest()


def extrapolate_user(token):
    cleaned_token = token.split("=")[1]
    part_containing_id = cleaned_token.split('-')[0]
    return int(re.split('[^0-9.]', part_containing_id)[0])
