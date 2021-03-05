from django.contrib import admin
from django.urls import path
from orikomi.views import IndexView, signupfunc

app_name = 'orikomi'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', signupfunc, name='index'),

]
