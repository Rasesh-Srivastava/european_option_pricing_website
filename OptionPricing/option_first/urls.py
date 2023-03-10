from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='option-home'),
    path('black/', views.black,name='black-scholes'),

]