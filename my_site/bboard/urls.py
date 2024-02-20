from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name="index"),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index_default')
]