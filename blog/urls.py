from django.urls import path
from blog import views

urlpatterns = [
    path('<str:each_id>', views.detail, name = 'urlnamedetail'),
    path('new/', views.new, name = 'urlnamenew'),
    path('create/', views.create, name = 'urlnamecreate'),
    path('edit/<str:each_id>', views.edit, name = 'urlnameedit'),
    path('update/<str:each_id>', views.update, name ='urlnameupdate'),
    path('delete/<str:each_id>', views.delete, name = 'urlnamedelete')
]