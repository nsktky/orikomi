# Generated by Django 3.1.7 on 2021-05-03 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(choices=[('kyusyu', '九州・沖縄'), ('sikoku', '四国'), ('tyugoku', '中国'), ('kinki', '近畿'), ('tyubu', '中部'), ('kanto', '関東'), ('tohoku', '東北'), ('hokkaido', '北海道')], max_length=8, verbose_name='上演地域')),
            ],
            options={
                'verbose_name_plural': 'area',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(choices=[('drama', '演劇'), ('musical', 'ミュージカル'), ('live', 'ライブ'), ('dance', 'ダンス'), ('opera', 'オペラ'), ('concert', 'コンサート'), ('ballet', 'バレエ'), ('kabuki', '歌舞伎'), ('geino', '伝統芸能（能、狂言、文楽）'), ('rakugo', '落語'), ('other', 'その他')], max_length=9, verbose_name='ジャンル')),
            ],
            options={
                'verbose_name_plural': 'genre',
            },
        ),
        migrations.CreateModel(
            name='Orikomi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='公演名')),
                ('start_day', models.DateField(verbose_name='上演開始日')),
                ('end_day', models.DateField(verbose_name='上演終了日')),
                ('front_imege', models.ImageField(upload_to='front_imeges/', verbose_name='チラシ表面')),
                ('back_image', models.ImageField(blank=True, null=True, upload_to='back_imeges/', verbose_name='チラシ裏面')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orikomi.area', verbose_name='上演地域')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orikomi.genre', verbose_name='ジャンル')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'orikomi',
            },
        ),
    ]
