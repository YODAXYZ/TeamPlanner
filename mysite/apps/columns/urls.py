from django.contrib import admin
from django.urls import path
from columns import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:column_id>/<int:board_id>', views.detail, name='detail'),
    path('create_column/<int:board_id>/', views.create_column, name="create_column"),
    # path('', views.create_column, name="create_column"),
    # path('show_column', views.show_column),  # наверное тут надо будет на страницу доски кидать
    path('edit_column/<int:id>', views.edit_column),
    path('update_column/<int:id>', views.update_column),
    path('delete_column/<int:column_id>/<int:board_id>', views.delete_column),
    # path('create_task', views.create_task),
    # # path('show_task', views.show_task),  # наверное тут надо будет на страницу доски кидать
    # path('edit_task/<int:id>', views.edit_task),
    # path('update_task/<int:id>', views.update_task),
    # path('delete_task/<int:id>', views.delete_task),
]
