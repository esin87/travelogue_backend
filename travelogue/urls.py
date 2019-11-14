from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('entries', views.EntryList, name='entry_list'),
    path('entries/<int:pk>', views.EntryDetail, name='entry_detail'),
]
