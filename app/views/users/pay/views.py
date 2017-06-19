from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from app.decorators import user_is_authenticated


@require_http_methods(["POST"])
@user_is_authenticated
def update_dd_info(request, user_id):
    return HttpResponse("Update dd info for user " + str(user_id))


@require_http_methods(["POST"])
@user_is_authenticated
def decrypt_bank_acct_num(request, user_id):
    return HttpResponse("Decrypt the bank info " + str(user_id))


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_pay_index(request, user_id):
    return HttpResponse("Pay index for user " + str(user_id))


@require_http_methods(["GET"])
@user_is_authenticated
def new_user_pay(request, user_id):
    return HttpResponse("New pay for " + str(user_id))


@require_http_methods(["GET"])
@user_is_authenticated
def edit_user_pay(request, user_id, id):
    return HttpResponse("Edit pay for user " + str(user_id) +
                        " for pay with id " + str(id))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
@user_is_authenticated
def user_pay(request, user_id, id):
    return HttpResponse("Pay for user " + str(user_id) +
                        " for pay with id " + str(id))
