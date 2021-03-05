from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.views.generic import TemplateView

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
            return render(request, 'signup.html', {'some': 100})
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは登録されています。'})

    return render(request, 'signup.html')