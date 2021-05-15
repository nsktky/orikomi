from accounts.models import CustomUser
from django.db import models


class Area(models.Model):
    # 上演地域用DB。area_jpは可読性のある表記用カラム
    area = models.CharField(verbose_name='上演地域(DB値)', max_length=30, primary_key=True)
    area_jp = models.CharField(verbose_name='上演地域(web上表記)', max_length=30)

    class Meta:
        verbose_name_plural='area'
    # area_jpを返し、ユーザが読めるようにする。
    def __str__(self):
        return self.area_jp


class Genre(models.Model):
    genre = models.CharField(verbose_name='ジャンル（DB値）', max_length=30, primary_key=True)
    genre_jp = models.CharField(verbose_name='ジャンル（web上表記）', max_length=30)

    class Meta:
        verbose_name_plural='genre'

    def __str__(self):
        return self.genre_jp


class Orikomi(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='公演名', max_length=150)
    start_day = models.DateField(verbose_name='上演開始日')
    end_day = models.DateField(verbose_name='上演終了日')
    area = models.ForeignKey(Area, verbose_name='上演地域', to_field='area', on_delete=models.PROTECT)
    genre = models.ForeignKey(Genre, verbose_name='ジャンル', to_field='genre', on_delete=models.PROTECT)
    front_imege = models.ImageField(verbose_name='チラシ表面')
    back_image = models.ImageField(verbose_name='チラシ裏面', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural='orikomi'

    def __str__(self):
        return self.title