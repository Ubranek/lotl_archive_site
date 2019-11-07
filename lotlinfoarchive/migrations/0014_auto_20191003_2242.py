# Generated by Django 2.1.5 on 2019-10-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotlinfoarchive', '0013_auto_20191003_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text_full_de',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='article',
            name='text_full_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='article',
            name='text_full_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='article',
            name='text_short_de',
            field=models.TextField(null=True, verbose_name='Анонс'),
        ),
        migrations.AddField(
            model_name='article',
            name='text_short_en',
            field=models.TextField(null=True, verbose_name='Анонс'),
        ),
        migrations.AddField(
            model_name='article',
            name='text_short_ru',
            field=models.TextField(null=True, verbose_name='Анонс'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_de',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]
