from django.contrib import admin
from django.urls import path
from orikomi.views import IndexView, InquiryView, signupfunc, loginfunc, logoutfunc, MenuView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('inquiry/', InquiryView.as_view(), name='inquiry'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('login/', logoutfunc, name='logout'),
    path('menu/', MenuView.as_view(), name='menu'),

]
