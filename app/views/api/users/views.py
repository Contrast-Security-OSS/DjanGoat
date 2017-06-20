from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from app.models import User
from django.core import serializers
from Crypto.Hash import SHA
from pygoat.settings import ACCESS_TOKEN_SALT
import re
import urlparse


@require_http_methods(["GET"])
def api_index(request):
    id, hash = split_token_into_id_token(request)
    if check_if_valid_token(id, hash):
        try:
            user = User.objects.get(user_id=id)
            if user.is_admin:
                data = serializers.serialize("json", User.objects.all())
                return HttpResponse(data, content_type='application/json')
            else:
                data = serializers.serialize("json", User.objects.filter(user_id=id))
                return HttpResponse(data, content_type='application/json')
        except User.DoesNotExist:
            return HttpResponse("null", content_type='application/json')
    else:
        return HttpResponse('Unauthorized', status=401)


@require_http_methods(["GET"])
def api(request, id_number):
    id, hash = split_token_into_id_token(request)
    if check_if_valid_token(id, hash):
        data = serializers.serialize("json", User.objects.filter(user_id=id))
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponse('Unauthorized', status=401)


def split_token_into_id_token(request):
    if 'HTTP_AUTHORIZATION' not in request.META:
        return None, None
    else:
        token = urlparse.unquote(request.META['HTTP_AUTHORIZATION'])
        regex = re.compile("(.*?)-(.*)")
        regex_groups = regex.search(token)
        if regex_groups.group(1):
            print(regex_groups.group(0))
            id = regex_groups.group(1).split('=')[0]
        else:
            return None, None
        if regex_groups.group(2):
            hash = regex_groups.group(2)
        else:
            return None, None

        return id, hash


# This is purposely vulnerable see - https://github.com/OWASP/railsgoat/wiki/Extras:-Broken-Regular-Expression
def check_if_valid_token(id, hash):
    if id is None or hash is None:
        return False

    sha = SHA.new()
    sha.update(ACCESS_TOKEN_SALT + ":" + str(id))
    return hash == sha.hexdigest()


def extrapolate_user(token):
    print token
