from django.urls import path
from .views import BuyerList, BuyerDetail, \
      SellerList, SellerDetail, TransactionList, \
      TransactionDetail


urlpatterns = [
    path('buyer', BuyerList.as_view()),
    path('buyer/<pk>', BuyerDetail.as_view()),
    path('seller', SellerList.as_view()),
    path('seller/<pk>', SellerDetail.as_view()),
    path('transaction', TransactionList.as_view()),
    path('transaction/<pk>', TransactionDetail.as_view()),
    
]