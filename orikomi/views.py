from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, FormView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InquiryForm, OrikomiCreateForm, OrikomiSearchForm
from .models import Orikomi

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


# ログイン後メニュー画面
class MenuView(LoginRequiredMixin, ListView):
    model = Orikomi
    template_name = 'menu.html'

    # DB上のユーザーとログインユーザーが一致するものだけをfilterで抽出
    def get_queryset(self):
        qs = Orikomi.objects.filter(user=self.request.user).order_by('-created_at')
        return qs


# オリコミ詳細画面
class OrikomiDetailView(LoginRequiredMixin, DetailView):
    model = Orikomi
    template_name = 'orikomi_detail.html'


class OrikomiCreateView(LoginRequiredMixin, CreateView):
    model = Orikomi
    template_name = 'orikomi_create.html'
    form_class = OrikomiCreateForm
    success_url = reverse_lazy('orikomi:menu')

    # フォームバリデーションに問題なければ下記メソッド実行。form_validメソッドをオーバーライドで実装
    def form_valid(self, form):
        # formではユーザー名を求めないのでcommit=FalseでDBに保存せずオブジェクト化
        qs = form.save(commit=False)
        # オブジェクトのユーザーにリクエストユーザーを上書き
        qs.user = self.request.user
        # DBに保存
        qs.save()
        messages.success(self.request, 'チラシをオリコミしました。')
        return super().form_valid(form)

    # フォームバリデーションに問題あればエラー文を返す。
    def form_invalid(self, form):
        messages.error(self.request, 'オリコミできませんでした。もう一度入力し直して下さい。')
        return super().form_invalid(form)


class OrikomiUpdatelView(LoginRequiredMixin, UpdateView):
    model = Orikomi
    template_name = 'orikomi_update.html'
    form_class = OrikomiCreateForm

    # urlが動的に変化するためget_success_urlをオーバーライドしpkを渡す。
    def get_success_url(self):
        return reverse_lazy('orikomi:orikomi_detail', kwargs={'pk':self.kwargs['pk']})

    # フォームバリデーションに問題なければ成功文を返す。
    def form_valid(self, form):
        messages.success(self.request, 'オリコミを更新しました。')
        return super().form_valid(form)

    # フォームバリデーションに問題あればエラー文を返す。
    def form_invalid(self, form):
        messages.error(self.request, 'オリコミを更新できませんでした。もう一度入力し直して下さい。')
        return super().form_invalid(form)


class OrikomiDeleteView(LoginRequiredMixin, DeleteView):
    model = Orikomi
    template_name = 'orikomi_delete.html'
    success_url = reverse_lazy('orikomi:menu')

    # deleteメソッドをオーバーライドし削除メッセージを渡す。
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'オリコミを削除しました。')
        return super().delete(request, *args, **kwargs)


class OrikomiWatchVIew(ListView):
    model = Orikomi
    template_name = 'orikomi_watch.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = OrikomiSearchForm(self.request.GET or None)
        return context