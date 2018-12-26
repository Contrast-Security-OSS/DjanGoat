from __future__ import unicode_literals
# Django imports
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.utils import timezone

# App imports
from app.models.Pay.pay import Pay
from app.decorators import user_is_authenticated
from app.views import utils


@require_http_methods(["POST"])
@user_is_authenticated
def update_dd_info(request, user_id):
    curr_user = utils.current_user(request)
    form = request.POST
    if not form:
        return HttpResponse("Pay index")

    Pay.objects.create(user=curr_user,
                       bank_account_num=form['bankAccNumInput'],
                       bank_routing_num=form['bankRouteNumInput'],
                       percent_of_deposit=form['percentDepositInput'],
                       created_at=timezone.now(), updated_at=timezone.now())

    return HttpResponseRedirect('/users/' + str(user_id) + '/pay')


@require_http_methods(["POST"])
@user_is_authenticated
def decrypt_bank_acct_num(request, user_id):  # pylint: disable=unused-argument
    form = request.POST
    if not form:
        return HttpResponse("No form")

    account_num = request.POST['account_number']
    curr_user = utils.current_user(request)
    response = HttpResponse()
    try:
        pay = Pay.objects.get(
            user=curr_user, bank_account_num=account_num
        )
        decrypted_account_num = pay.decrypt_bank_num()
        response['success'] = True
        response.content = decrypted_account_num
        return response
    except Pay.DoesNotExist:
        response['success'] = False
        return response


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_pay_index(request, user_id):  # pylint: disable=unused-argument
    user = utils.current_user(request)
    if user is not None:
        direct_deposits = Pay.objects.filter(user=user)
        return render(request, 'users/pay/index.html',
                      {'current_user': user,
                       'direct_deposits': direct_deposits})
    else:
        return HttpResponseRedirect('/signup')


@require_http_methods(["DELETE"])
@user_is_authenticated
def user_pay(request, user_id, pay_id):
    if request.method == "DELETE":
        Pay.objects.get(id=pay_id).delete()
        return HttpResponse("Success!")

    return HttpResponse("Pay for user " +
                        str(user_id) + " for pay with id " + str(pay_id))
