# Generated by Django 2.1.5 on 2019-04-06 19:26

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('for_dev_tests', '0003_auto_20190128_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpletranslationmodel',
            name='test_image_field',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Изображение', to=settings.FILER_IMAGE_MODEL),
        ),
    ]