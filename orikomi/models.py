from accounts.models import CustomUser
from django.db import models


class Area(models.Model):
    area = models.CharField(verbose_name='上演地域', max_length=30, primary_key=True)

    class Meta:
        verbose_name_plural='area'

    def __str__(self):
        return self.area


class Genre(models.Model):
    genre = models.CharField(verbose_name='ジャンル', max_length=30, primary_key=True)

    class Meta:
        verbose_name_plural='genre'

    def __str__(self):
        return self.genre


class Orikomi(models.Model):
    AREA_SELECT = (
        ('kyusyu', '九州・沖縄'),
        ('sikoku', '四国'),
        ('tyugoku', '中国'),
        ('kinki', '近畿'),
        ('tyubu', '中部'),
        ('kanto', '関東'),
        ('tohoku', '東北'),
        ('hokkaido', '北海道'),
    )

    GENRE_SELECT = (
        ('drama', '演劇'),
        ('musical', 'ミュージカル'),
        ('live', 'ライブ'),
        ('dance', 'ダンス'),
        ('opera', 'オペラ'),
        ('concert', 'コンサート'),
        ('ballet', 'バレエ'),
        ('kabuki', '歌舞伎'),
        ('geino', '伝統芸能（能、狂言、文楽）'),
        ('rakugo', '落語'),
        ('other', 'その他'),
    )

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='公演名', max_length=150)
    start_day = models.DateField(verbose_name='上演開始日')
    end_day = models.DateField(verbose_name='上演終了日')
    area = models.ForeignKey(Area, verbose_name='上演地域', to_field='area', on_delete=models.PROTECT, choices=AREA_SELECT)
    genre = models.ForeignKey(Genre, verbose_name='ジャンル', to_field='genre', on_delete=models.PROTECT, choices=GENRE_SELECT)
    front_imege = models.ImageField(verbose_name='チラシ表面')
    back_image = models.ImageField(verbose_name='チラシ裏面', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural='orikomi'

    def __str__(self):
        return self.title