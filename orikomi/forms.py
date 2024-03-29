from django import forms
from django.core.mail import EmailMessage
from .models import Orikomi, Area, Genre
import os

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=50)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル', max_length=100)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-12'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前'
        self.fields['email'].widget.attrs['class'] = 'form-control col-12'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレス'
        self.fields['title'].widget.attrs['class'] = 'form-control col-12'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトル'
        self.fields['message'].widget.attrs['class'] = 'form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージ内容'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ {}'.format(title)
        message = '送信者名：{0}\nメールアドレス：{1}\nタイトル：{2}\nメッセージ：{3}'.format(name, email, title, message)
        from_email = 'admin@example.com'
        to_list = [
            'test@example.com'
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()


class OrikomiCreateForm(forms.ModelForm):
    class Meta:
        model = Orikomi
        fields = ('title', 'start_day', 'end_day', 'area', 'genre', 'front_imege', 'back_image')
        # 日付入力蘭をプルダウンにするためwigetsを設定
        widgets = {
            'start_day': forms.SelectDateWidget,
            'end_day': forms.SelectDateWidget,
        }

class OrikomiSearchForm(forms.ModelForm):
    class Meta:
        model = Orikomi
        fields = ('area', 'genre')