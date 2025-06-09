from django.urls import path
from .views import add_money, add_money_confirmation

urlpatterns = [
    path("add-money/", add_money, name="add_money"),
    path("add-money-confirmation/", add_money_confirmation, name="add_money_confirmation"),
]