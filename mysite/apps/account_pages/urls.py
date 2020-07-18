from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='account_pages'),
    path('create_board/', views.create_board),
]