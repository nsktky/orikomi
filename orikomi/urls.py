from django.contrib import admin
from django.urls import path
from orikomi.views import IndexView, InquiryView, MenuView, OrikomiDetailView, OrikomiCreateView, OrikomiUpdatelView

app_name = 'orikomi'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('inquiry/', InquiryView.as_view(), name='inquiry'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('orikomi_detail/<int:pk>/', OrikomiDetailView.as_view(), name='orikomi_detail'),
    path('orikomi_create/', OrikomiCreateView.as_view(), name='orikomi_create'),
    path('orikomi_update/<int:pk>/', OrikomiUpdatelView.as_view(), name='orikomi_update'),

]
