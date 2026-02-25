from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ajax/submit/', views.ajax_submit, name='ajax_submit'),
    path('ajax/delete/', views.ajax_delete, name='ajax_delete'),
    path('ajax/edit/', views.ajax_edit, name='ajax_edit'),
    path('ajax/update/', views.ajax_update, name='ajax_update'),
]