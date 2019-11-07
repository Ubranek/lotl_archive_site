# Generated by Django 2.1.5 on 2019-10-03 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotlinfoarchive', '0010_auto_20190811_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='album',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='album',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='event',
            name='anons_de',
            field=models.TextField(blank=True, null=True, verbose_name='Анонс'),
        ),
        migrations.AddField(
            model_name='event',
            name='anons_en',
            field=models.TextField(blank=True, null=True, verbose_name='Анонс'),
        ),
        migrations.AddField(
            model_name='event',
            name='anons_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Анонс'),
        ),
        migrations.AddField(
            model_name='event',
            name='title_de',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='event',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='event',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='lotlteammember',
            name='comment_de',
            field=models.TextField(blank=True, help_text='Можно прокомментировать, если хочется', null=True, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='lotlteammember',
            name='comment_en',
            field=models.TextField(blank=True, help_text='Можно прокомментировать, если хочется', null=True, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='lotlteammember',
            name='comment_ru',
            field=models.TextField(blank=True, help_text='Можно прокомментировать, если хочется', null=True, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='musician',
            name='info_de',
            field=models.TextField(null=True, verbose_name='Инфо'),
        ),
        migrations.AddField(
            model_name='musician',
            name='info_en',
            field=models.TextField(null=True, verbose_name='Инфо'),
        ),
        migrations.AddField(
            model_name='musician',
            name='info_ru',
            field=models.TextField(null=True, verbose_name='Инфо'),
        ),
        migrations.AddField(
            model_name='musician',
            name='name_de',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='musician',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='musician',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='musician',
            name='role_de',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Роль в группе (инструменты)'),
        ),
        migrations.AddField(
            model_name='musician',
            name='role_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Роль в группе (инструменты)'),
        ),
        migrations.AddField(
            model_name='musician',
            name='role_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Роль в группе (инструменты)'),
        ),
        migrations.AddField(
            model_name='textinfoblock',
            name='name_de',
            field=models.CharField(help_text='Для отображения в даминке (в основном', max_length=255, null=True, verbose_name='Заголовое'),
        ),
        migrations.AddField(
            model_name='textinfoblock',
            name='name_en',
            field=models.CharField(help_text='Для отображения в даминке (в основном', max_length=255, null=True, verbose_name='Заголовое'),
        ),
        migrations.AddField(
            model_name='textinfoblock',
            name='name_ru',
            field=models.CharField(help_text='Для отображения в даминке (в основном', max_length=255, null=True, verbose_name='Заголовое'),
        ),
        migrations.AddField(
            model_name='textinfoblock',
            name='text_de',
            field=models.TextField(blank=True, null=True, verbose_name='Текстовый блок информации'),
        ),
        migrations.AddField(
            model_name='textinfoblock',
            name='text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Текстовый блок информации'),
        ),
        migrations.AddField(
            model_name='textinfoblock',
            name='text_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Текстовый блок информации'),
        ),
        migrations.AddField(
            model_name='textmaterial',
            name='text_full_de',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='textmaterial',
            name='text_full_en',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='textmaterial',
            name='text_full_ru',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='textmaterial',
            name='text_short_de',
            field=models.TextField(null=True, verbose_name='Анонс'),
        ),
        migrations.AddField(
            model_name='textmaterial',
            name='text_short_en',
            field=models.TextField(null=True, verbose_name='Анонс'),
        ),
        migrations.AddField(
            model_name='textmaterial',
            name='text_short_ru',
            field=models.TextField(null=True, verbose_name='Анонс'),
        ),
        migrations.AddField(
            model_name='textmaterial',
            name='title_de',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='textmaterial',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='textmaterial',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='tour',
            name='description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='tour',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='tour',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='videolink',
            name='description_de',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='videolink',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='videolink',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='videolink',
            name='title_de',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='videolink',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='videolink',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='videolink',
            name='dt_published',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
    ]