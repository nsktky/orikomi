from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

def signupfunc(request):
    return render(request, 'signup.html', {})