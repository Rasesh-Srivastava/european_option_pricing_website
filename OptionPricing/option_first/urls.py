from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='option-home'),
    # path('home/', views.home,name='home'),
    path('twoStep/', views.twoStep,name='twoStep'),
    path('nStep/', views.nStep,name='nStep'),
    path('black/', views.black,name='black-scholes'),
    # path('stock/', C:\Users\rapti\Desktop\OptionPricing\option_first\templates\option_first\stock.jpg,name='image1'),

]