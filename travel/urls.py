# Module 0
from django.urls import path, include
from . import views  #import everything from views module
app_name = 'travel'

urlpatterns = [
    path('',views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),

    path('create', views.create, name='create'),
    path('loguser', views.login_user, name='loguser'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),
]
