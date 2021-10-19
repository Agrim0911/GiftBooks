from django.contrib import admin
from django.urls import path
from . import views

app_name= 'BookApp'
urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/',views.login,name='login'),
    path('',views.index,name='index'),
    path('loggedin/',views.log_index,name='loggedin'),
    path('add_book/',views.add_book,name='add_book'),
    path('detail/<int:id>/',views.detail,name='detail')
]
