# Generated by Django 2.2.4 on 2023-05-22 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_app', '0008_auto_20230521_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='title',
            field=models.CharField(max_length=10, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='account',
            name='type',
            field=models.IntegerField(verbose_name='类型'),
        ),
    ]
