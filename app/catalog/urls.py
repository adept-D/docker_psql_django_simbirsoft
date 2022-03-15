from unicodedata import name
from django import views
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.user_login, name='user_login'),
    path('accounts/logout/', views.user_logout, name='user_logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add_note/', views.add_note, name='add_note'),
    path('notes/', views.get_notes, name='notes'),
]
