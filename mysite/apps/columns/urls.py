from django.contrib import admin
from django.urls import path
from columns import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('column_new', views.column_new),
    path('show', views.show), # наверное тут надо будет на страницу доски кидать
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]