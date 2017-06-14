from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def update_dd_info(request, user_id):
    return HttpResponse("Update dd info for user " + str(user_id))


@require_http_methods(["POST"])
def decrypt_bank_acct_num(request, user_id):
    return HttpResponse("Decrypt the bank info " + str(user_id))


@require_http_methods(["GET", "POST"])
def user_pay_index(request, user_id):
    return HttpResponse("Pay index for user " + str(user_id))


@require_http_methods(["GET"])
def new_user_pay(request, user_id):
    return HttpResponse("New pay for " + str(user_id))


@require_http_methods(["GET"])
def edit_user_pay(request, user_id, id):
    return HttpResponse("Edit pay for user " + str(user_id) +
                        " for person with id " + str(id))


@require_http_methods(["GET", "PATCH", "PUT", "DELETE"])
def user_pay(request, user_id, id):
    return HttpResponse("Pay for user " + str(user_id) +
                        " for person with id " + str(id))
