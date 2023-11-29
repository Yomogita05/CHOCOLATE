from django.db import models

# Create your models here.

from accounts.models import CustomUser


class Channel1_data(models.Model):
    # タイトル
    name = models.CharField(
        verbose_name="名前",
        max_length=50
    )
    
    # 本文用のフィールド
    content = models.TextField(
        verbose_name="本文",
        max_length=200
    )

    # 投稿日時
    posted_at = models.DateTimeField(
        verbose_name="投稿日時",
        auto_now_add=True
    )
    
    def __str__(self):
        return self.content

class Channel2_data(models.Model):   
    name = models.CharField(
        verbose_name="名前",
        max_length=50
    )
    
    # 本文用のフィールド
    content = models.TextField(
        verbose_name="本文",
        max_length=200
    )

    # 投稿日時
    posted_at = models.DateTimeField(
        verbose_name="投稿日時",
        auto_now_add=True
    )
    
    def __str__(self):
        return self.content

class Channel3_data(models.Model):
    name = models.CharField(
        verbose_name="名前",
        max_length=50
    )
    
    # 本文用のフィールド
    content = models.TextField(
        verbose_name="本文",
        max_length=200
    )

    # 投稿日時
    posted_at = models.DateTimeField(
        verbose_name="投稿日時",
        auto_now_add=True
    )
    
    def __str__(self):
        return self.content

