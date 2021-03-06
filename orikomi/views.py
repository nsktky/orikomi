from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView

class IndexView(TemplateView):
    template_name = 'index.html'

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
            return redirect('orikomi:menu')
        else:
            return render(request, 'login.html', {'error': 'ユーザー名またはパスワードが間違っています。'})
    return render(request, 'login.html', {})


# ログイン後のメニューを実装
# ログインしてなければLOGIN_URLにリダイレクトするようデコレーターをつける
# @login_required
class MenuView(TemplateView):
    template_name = 'menu.html'