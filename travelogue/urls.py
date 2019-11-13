from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('entries', views.EntryList.as_view(), name='entry_list'),
    path('entries/<int:pk>', views.EntryDetail.as_view(), name='entry_detail'),
]
