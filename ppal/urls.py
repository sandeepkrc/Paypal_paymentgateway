from .views import checkout,store,paymentcomplete
from django.urls import path

urlpatterns = [

    path('checkout/<int:pk>',checkout,name="checkout"),
    path('complete',paymentcomplete,name="complete"),
    path('',store,name='store'),              
               ]
