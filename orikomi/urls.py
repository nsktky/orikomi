from django.contrib import admin
from django.urls import path
from orikomi.views import IndexView, signupfunc, loginfunc, MenuView

app_name = 'orikomi'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('menu/', MenuView.as_view(), name='menu'),

]
