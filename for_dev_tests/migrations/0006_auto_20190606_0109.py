# Generated by Django 2.1.5 on 2019-06-05 22:09

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('for_dev_tests', '0005_simpletranslationmodel_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpletranslationmodel',
            name='test_image_field',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='img_test', to=settings.FILER_IMAGE_MODEL),
        ),
    ]