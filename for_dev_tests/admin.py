from django.contrib import admin
from .models import SimpleTranslationModel

from modeltranslation.admin import TranslationAdmin
# Register your models here.

class NewsAdmin(TranslationAdmin):
    pass

admin.site.register(SimpleTranslationModel, NewsAdmin)