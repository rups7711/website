# Generated by Django 2.0.8 on 2019-03-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_headlines'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headlines',
            name='pic',
        ),
        migrations.AlterField(
            model_name='headlines',
            name='url',
            field=models.URLField(verbose_name='地址'),
        ),
    ]
