from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.create_task),
    # path('create_comment', views.create_comment),
    # path('show_comment', views.show_comment),  # наверное тут надо будет на страницу доски кидать
    path('edit_comment/<int:id>', views.edit_comment),
    path('update_comment/<int:id>', views.update_comment),
    path('delete_comment/<int:id>', views.delete_comment),
]
