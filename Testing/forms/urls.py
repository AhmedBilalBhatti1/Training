from django.urls import path
from . import views

urlpatterns = [
    path('',views.my_form_view,name='my_form'),
]
