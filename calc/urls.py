from django.contrib import admin

from django.urls import path,include

from . import views


urlpatterns = [
   # path('',include('calc.urls')),
    path('',views.home,name='home'),
    #path('new/', views.new, name = 'new'),
]
