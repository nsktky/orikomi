from accounts.models import CustomUser
from django.db import models

class Orikomi(models.Model):
    area_select = (
        ('kyusyu', '九州・沖縄'),
        ('sikoku', '四国'),
        ('tyugoku', '中国'),
        ('kinki', '近畿'),
        ('tyubu', '中部'),
        ('kanto', '関東'),
        ('tohoku', '東北'),
        ('hokkaido', '北海道'),
    )

    genre_select = (
        ('engeki', '演劇'),
        ('myuzikaru', 'ミュージカル'),
        ('raibu', 'ライブ'),
        ('dance', 'ダンス'),
        ('opera', 'オペラ'),
        ('concerte', 'コンサート'),
        ('bare', 'バレエ'),
        ('kabuki', '歌舞伎'),
        ('geino', '伝統芸能（能、狂言、文楽）'),
        ('rakugo', '落語'),
        ('other', 'その他'),
    )

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='公演名', max_length=150)
    start_day = models.DateField(verbose_name='上演開始日')
    end_day = models.DateField(verbose_name='上演終了日')
    area = models.CharField(verbose_name='上演地域', max_length=8, choices=area_select)
    genre = models.CharField(verbose_name='ジャンル', max_length=9, choices=genre_select)
    front_imege = models.ImageField(verbose_name='チラシ表面', upload_to='front_image/')
    back_image = models.ImageField(verbose_name='チラシ裏面', upload_to='back_image/', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural='orikomi'

    def __str__(self):
        return self.title