from django.urls import path

from . import views

urlpatterns = [
    path('get_cards', views.get_cards),
    path('add_new_cards', views.addnewcard),
    path('get_cards/<int:account_id>', views.change_password),
    path('pay_to', views.pay_to),
    path('show_month_bill', views.show_month_bill),
    path('add_new_examiner', views.add_new_examiner),
    path('get_applications', views.get_applications),

]