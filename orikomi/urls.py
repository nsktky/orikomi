from django.contrib import admin
from django.urls import path
from orikomi.views import IndexView, InquiryView, MenuView

app_name = 'orikomi'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('inquiry/', InquiryView.as_view(), name='inquiry'),
    path('menu/', MenuView.as_view(), name='menu'),

]
