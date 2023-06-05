# accounting_app/models.py
from django.db import models
from django.contrib.auth.models import User,AbstractUser
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=64)
    password = models.CharField(verbose_name='密码', max_length=128)

class Account(models.Model):

    title = models.CharField(max_length=10, verbose_name='标题')
    time = models.DateTimeField(verbose_name='时间')
    type = models.IntegerField( verbose_name='类型')
    account = models.FloatField(verbose_name='金额', max_length=10)
    remarks = models.TextField(blank=True, verbose_name='备注')

    #python manage.py makemigrations
    #python manage.py migrate

    def __str__(self):
        return self.title
