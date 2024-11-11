from django.urls import path
from . import views

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),  # Root for transactions list
    path('add/', views.add_transaction, name='add_transaction'),  # Add transaction
]
