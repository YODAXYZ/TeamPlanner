from django.urls import path
from . import views

app_name = 'room'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:room_id>/', views.detail, name='detail'),
    # path('leave_post/', views.leave_post, name='leave_post'),
]