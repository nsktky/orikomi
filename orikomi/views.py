from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import InquiryForm

class IndexView(TemplateView):
    template_name = 'index.html'

# お問い合わせ用フォーム
class InquiryView(FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('orikomi:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        return super().form_valid(form)


class MenuView(TemplateView):
    template_name = 'menu.html'