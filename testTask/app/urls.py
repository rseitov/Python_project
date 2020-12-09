from django.urls import path
from app import views

urlpatterns = [
    path('', views.directory, name = 'directory'),
    path('add', views.add_directory,  name = 'add_directory'),
    path('sp/<id>', views.get_sp_info,  name = 'get_sp_info'),
    path('sp/<id>/edit', views.edit_elemet, name = 'edit_elemet'),
    path('sp/<id>/delete', views.delete_element, name='delete_element'),
    path('element/add', views.add_el_direct,name='add_el_direct'),
    path('val/<id>/delete', views.delete_el_direct, name='delete_el_direct'),
    path('val/<id>/edit', views.edit_elemet_direct, name = 'edit_elemet_direct'),

]
