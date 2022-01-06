
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('func_signup', views.func_signup, name='func_signup'),
    path('func_login', views.func_login, name='func_login'),
    path('func_logout', views.func_logout, name='func_logout'),
]
