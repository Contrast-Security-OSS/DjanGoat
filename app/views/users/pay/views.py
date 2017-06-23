from __future__ import unicode_literals

from django.views.decorators.http import require_http_methods
from app.decorators import user_is_authenticated

from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from app.views import utils
from app.models import Pay
from django.utils import timezone


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
def decrypt_bank_acct_num(request, user_id):
    form = request.POST
    if not form:
        return HttpResponse("No form")

    account_num = request.POST['account_number']
    curr_user = utils.current_user(request)
    pay = Pay.objects.get(
        user=curr_user, bank_account_num=account_num
    )
    decrypted_account_num = pay.decrypt_bank_num()
    return HttpResponse(decrypted_account_num)


@require_http_methods(["GET", "POST"])
@user_is_authenticated
def user_pay_index(request, user_id):
    template = get_template('users/pay/index.html')
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
def user_pay(request, user_id, id):
    if request.method == "DELETE":
        Pay.objects.get(id=id).delete()
        return HttpResponse("Success!")

    return HttpResponse("Pay for user " +
                        str(user_id) + " for pay with id " + str(id))
