# login/models.py

from django.db import models


class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    user_name = models.CharField(max_length=128, unique=True)
    nickname = models.CharField(max_length=128, unique=True )
    password = models.CharField(max_length=256)
    mobile = models.CharField(max_length=11)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
