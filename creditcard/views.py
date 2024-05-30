import datetime
import json
from django.core import serializers
from django.core.serializers import serialize
from django.db.models import Sum
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import *


## 信用卡操作部分
@require_http_methods(["GET"])
def get_cards(request):
    """
    show all cards, return all credit cards
    """
    response = {}
    try:
        cards = CreditCard.objects.filter()
        response['status'] = 'success'
        response['message'] = 'Cards show successfully.'
        response['error_num'] = 0
        response['cardlist'] = json.loads(serializers.serialize('json', cards))
    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def addnewcard(request):
    """
    create a new card and return the card
    """
    response = {}
    try:
        # Create a new credit card
        card = CreditCard().newcard()

        # Serialize the card object to JSON format
        card_json = serialize('json', [card], ensure_ascii=False)

        # Prepare the response dictionary
        response['status'] = 'success'
        response['message'] = 'Cards added successfully.'
        response['error_num'] = 0
        response['card'] = card_json

    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)
        response['error_num'] = 1

    # Use JsonResponse to return the response dictionary as JSON
    return JsonResponse(response)


@require_http_methods(["PUT"])
def change_password(request, account_id):
    """
    Change the password of a credit card and return the card
    """
    response = {}
    try:
        # Parse the JSON body of the request
        data = json.loads(request.body)

        # Fetch the credit card using the account_id from URL parameters
        card = CreditCard.objects.get(account_id=request.GET['account_id'])

        # Get the new password from the parsed data
        new_password = data['new_password']

        # Update the password
        card.modify_password(card, new_password=new_password)
        card.save()

        response['status'] = 'success'
        response['message'] = 'Password has been changed successfully.'
        response['error_num'] = 0

    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)
        response['error_num'] = 1

    # Use JsonResponse to return the response dictionary as JSON
    return JsonResponse(response)


## 账单操作部分
@require_http_methods(["GET"])
def pay_to(request):
    """
    add a record to the transfer_record
    """
    response = {}
    try:
        new_transaction = Transaction(
            account_in_id=request.GET['account_in_id'],
            account_out_id=request.GET['account_out_id'],
            transfer_amount=request.GET['amount'],
            transfer_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 使用当前时间作为交易日期
            # transfer_date=request.GET['date']
        )
        new_transaction.save()
        response['status'] = 'success'
        response['message'] = 'New transaction has been created and saved successfully.'
        response['error_num'] = 0
    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def show_month_bill(request):
    """
    'user' get the bill of 'year''month'
    """
    response = {}
    try:
        year = request.GET['year']
        month = request.GET['month']
        if not year or not month:
            raise ValueError("Year and month parameters are required.")
        bill = Transaction.objects.filter(
            account_in_id=request.GET['account_in_id'],
            transfer_date__year=year,
            transfer_date__month=month
        )
        response['total_amount'] = bill.aggregate(total=Sum('transfer_amount'))['total'] or 0
        response['list'] = json.loads(serializers.serialize('json', bill))
        response['status'] = 'success'
        response['message'] = 'All bills have been saved.'
        response['error_num'] = 0
    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def show_pay_info(request):
    """
    show the detail-information and result of a pay_record (show frontend result)
    """
    response = {}
    try:
        transaction = Transaction.objects.filter(
            transfer_record_id=request.GET['transfer_record_id'],
        )
        response['list'] = json.loads(serializers.serialize('json', transaction))
        response['status'] = 'success'
        response['message'] = 'All payment infos have been saved.'
        response['error_num'] = 0
    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def add_new_examiner(request, employee_id, sys_manager_id):
    """
    add a new examiner and return the examiner
    """
    response = {}
    sys_manager = SystemManager.objects.get(sys_manager_id=sys_manager_id)
    try:
        new_examiner = sys_manager.add_credit_examiner(employee_id=employee_id)
        new_examiner_json = serialize('json', [new_examiner], ensure_ascii=False)

        # Prepare the response dictionary
        response['status'] = 'success'
        response['message'] = 'Cards added successfully.'
        response['error_num'] = 0
        response['new_examiner'] = new_examiner_json

    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)
        response['error_num'] = 1

    # Use JsonResponse to return the response dictionary as JSON
    return JsonResponse(response)


def get_applications():
    """
    show all applications, return all applications
    """
    response = {}
    try:
        applications = CreditCardApplication.objects.filter()
        response['status'] = 'success'
        response['message'] = 'Applications show successfully.'
        response['error_num'] = 0
        response['applicationlist'] = json.loads(serializers.serialize('json', applications))
    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
