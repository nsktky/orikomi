from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from orikomi.views import IndexView, InquiryView, MenuView, OrikomiDetailView, \
    OrikomiCreateView, OrikomiUpdatelView, OrikomiDeleteView, OrikomiSearchView

app_name = 'orikomi'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('inquiry/', InquiryView.as_view(), name='inquiry'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('orikomi_detail/<int:pk>/', OrikomiDetailView.as_view(), name='orikomi_detail'),
    path('orikomi_create/', OrikomiCreateView.as_view(), name='orikomi_create'),
    path('orikomi_update/<int:pk>/', OrikomiUpdatelView.as_view(), name='orikomi_update'),
    path('orikomi_delete/<int:pk>/', OrikomiDeleteView.as_view(), name='orikomi_delete'),
    path('orikomi_search/', OrikomiSearchView.as_view(), name='orikomi_search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)