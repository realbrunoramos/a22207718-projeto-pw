from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('recover_password/', views.recover_password, name='recover_password'),
]
