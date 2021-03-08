from django.db import models
from django.contrib.auth.models import AbstractUser

# 拡張ユーザーモデル
class CustomUser(AbstractUser):

    class Meta:
        verbose_name_plural = 'CustomUser'