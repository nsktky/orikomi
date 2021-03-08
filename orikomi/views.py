from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
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


# サインイン関数。新規ユーザーの作成と重複登録を防ぐ処理をする
def signupfunc(request):
    # レスポンスがpostだった場合（signup.htmlのform入力があった場合）の動作
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # ユーザー作成時、重複していたらexcept
        try:
            # create_userでユーザーを作成。引数にユーザー名、メールアドレス、パスワードを渡す
            user = User.objects.create_user(username, '', password)
            # renderメソッドはhttpレスポンスを作成する
            return render(request, 'signup.html', {})
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは登録されています。'})

    return render(request, 'signup.html')


# ログイン関数。登録されたユーザーを認証する。
def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # ログイン成功したらmenuページへリダイレクト
            return redirect('menu')
        else:
            return render(request, 'login.html', {'error': 'ユーザー名またはパスワードが間違っています。'})
    return render(request, 'login.html', {})


# ログアウト機能。ログアウト後はtopページへ遷移
def logoutfunc(request):
    logout(request)
    return redirect('index')

# ログイン後のメニューを実装
# LoginRequiredMixinでログイン必須にする
class MenuView(TemplateView, LoginRequiredMixin):
    template_name = 'menu.html'