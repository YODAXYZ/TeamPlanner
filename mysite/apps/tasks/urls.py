from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_task),
    path('create_task/<int:column_id>/<int:board_id>', views.create_task,),
    path('delete_task/<int:task_id>/<int:column_id>/<int:board_id>', views.delete_task),
    path('edit_task/<int:task_id>/<int:column_id>/<int:board_id>', views.edit_task),
    # path('create_comment', views.create_comment),
    # path('edit_comment/<int:id>', views.edit_comment),
    # path('update_comment/<int:id>', views.update_comment),
    # path('delete_comment/<int:id>', views.delete_comment),
]
