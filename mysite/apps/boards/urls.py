from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('<int:board_id>/', views.detail, name='detail'),
    # path('leave_post/', views.leave_post, name='leave_post'),
]
