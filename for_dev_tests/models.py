from django.db import models
from django.utils.translation import gettext as _
from filer.fields.image import FilerImageField
from taggit_autosuggest.managers import TaggableManager

# Create your models here.
class SimpleTranslationModel(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255)
    body_text = models.TextField(_('Основной текст'))
    pub_date = models.DateTimeField(_('Дата публикации'), auto_now_add=True, blank=True)
    test_image_field = FilerImageField(null=True, blank=True,
                                       related_name=_("img_test"), on_delete=models.SET_NULL)
    tags = TaggableManager()

    class Meta:
        verbose_name=_('Тестовая модель для перевода')
        verbose_name_plural = _('Тесытовые модели для перевода')

    def __str__(self):
        return self.title


