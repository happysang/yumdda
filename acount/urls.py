from django.urls import path
from acount import views

urlpatterns = [
    path ('login/', views.login_view, name = 'urlnamelogin'),
    path ('logout/', views.logout_view, name = 'urlnamelogout'),
    path ('signup/', views.signup, name ='urlnamesignup'),
    path ('error/', views.error, name ='urlnameerror'),
    
]