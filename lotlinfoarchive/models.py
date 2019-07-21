from django.db import models
from django.utils.translation import gettext as _
from filer.fields.image import FilerImageField
from taggit_autosuggest.managers import TaggableManager

# Create your models here.

#Модель нужна для организации инлайн-датасетов в админке
buy_sources = (('0', 'Lord Of The Lost Online Shop'), ('1', 'iTunes'), ('2', _('Другoе')))
class BuyLink(models.Model):
    source = models.CharField(_('Название площадки'), choices=buy_sources, default='0', max_length=1)
    url = models.URLField(_('Ссылка на покупку'), help_text='Ссылка может быть использована повторно')
    is_main = models.BooleanField(_('Оф. магазин'), default=True)
    comment = models.CharField(_('Комментарий'), help_text='Ссылку можно прокомментировать, если хочется', blank=True, null=True, max_length=255)

    class Meta:
        verbose_name = _('Ссылка на покупку')
        verbose_name_plural = _('Ссылки на покупку')

    def __str__(self):
        return self.source


class LotlTeamMember(models.Model):
    name_nick = models.CharField(_('Ник (или имя)'), max_length=255)
    comment = models.TextField(_('Комментарий'), help_text='Можно прокомментировать, если хочется', blank=True, null=True)
    is_active = models.BooleanField(_('Активность'), default=True, help_text='Можно отметить уже не участвующих членов команды, если вдруг захочется их где-то вывести')

    class Meta:
        verbose_name = _('Участник команды LOTL-info')
        verbose_name_plural = _('Участники команды LOTL-info')

    def __str__(self):
        return self.name_nick

video_categories = ((0,_('Другое')), (1,_('Клип')),(2, 'TV of the Lost'), (3,_('Концертная запись')))
class VideoLink(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255)
    #slug = models.SlugField(_('Идентификатор ссылки '), unique=True, help_text='Заполняется автоматически по заголовку. В случае неуникальности добавить в конце цифру')
    dt_published = models.DateTimeField(_(''), auto_now_add=True)
    video_url = models.URLField('URL на ютуб (желательно)')
    author = models.CharField(_('Автор'), max_length=255, null=True, blank=True)
    description = models.TextField(_('Описание'), blank=True, null=True)
    is_official = models.BooleanField(_('Официальный материал'), default=True)
    category = models.IntegerField(_('Категория видео'), choices=video_categories, default=0)
    tags = TaggableManager(verbose_name=_('Теги'), blank=True)


    class Meta:
        verbose_name = _('Видео-ссылка')
        verbose_name_plural = _('Видео-ссылки')

    def __str__(self):
        return self.title

class Photo(models.Model):
    img = FilerImageField(null=True, blank=True,
                    related_name=_("Изображение"), help_text='Редактирование параметров картинки в отдельном приложении админки (Filer)', on_delete=models.SET_NULL)
    author = models.CharField(_('Автор'), max_length=255, null=True, blank=True)
    tags = TaggableManager(verbose_name=_('Ассоциированные теги'), blank=True)

class Tour(models.Model):
    name = models.CharField(_('Наименование тура'), max_length=255)
    slug = models.SlugField(_('Идентификатор ссылки '), unique=True, help_text='Заполняется автоматически по заголовку. В случае неуникальности добавить в конце цифру')
    description = models.TextField(_('Описание'),  blank=True, null=True)
    associated_tags = TaggableManager(verbose_name=_('Ассоциированные теги'))

    class Meta:
        verbose_name = _('Концертный тур')
        verbose_name_plural = _('Концертные туры')

    def __str__(self):
        return self.name

class Musician(models.Model):
    name = models.CharField(_('Имя'), max_length=255)
    slug = models.SlugField(_('Идентификатор ссылки '), unique=True, help_text='Заполняется автоматически по заголовку. В случае неуникальности добавить в конце цифру')
    real_name = models.CharField(_('Имя'), max_length=255, blank=True, null=True)
    role = models.CharField(_('Роль в группе (инструменты)'), max_length=255, blank=True, null=True)
    facebook = models.URLField('Facebook', max_length=255, blank=True, null=True)
    instagram = models.URLField('Facebook', max_length=255, blank=True, null=True)
    info = models.TextField('Инфо')
    is_active = models.BooleanField('Активный участник', default=True)
    photo = models.ManyToManyField(Photo,
                                       verbose_name=_("Фотографии"), through='MusicianPhoto')

    signature = FilerImageField(null=True, blank=True,
                                       related_name=_("Автограф"), on_delete=models.SET_NULL)
    associated_tags = TaggableManager(verbose_name=_('Ассоциированные теги'))

    class Meta:
        verbose_name = _('Участник группы')
        verbose_name_plural = _('Участники группы')

    def __str__(self):
        return self.name

class MusicianPhoto(models.Model):
    musician = models.ForeignKey(Musician, verbose_name=_('Музыкант'), on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, verbose_name=_('Фотография'), on_delete=models.CASCADE)
    is_cover = models.BooleanField(_('Основная фотка профиля'), default=False)

    class Meta:
        verbose_name = _('Фотография участника группы')
        verbose_name_plural = _('Фотографии участника группы')

    def __str__(self):
        is_cover = ""
        if (self.is_cover):
            is_cover = _("Основная")
        return self.musician + " " + is_cover


album_types = ((0,_('Другое')), (1,_('Электронный')), (2, _('Акустический (c оркестром)')), (3, _('Концертная запись')), (4, _('Сингл')), (5, _('Сборник')))
class Album(models.Model):
    name = models.CharField(_('Наименование альбома'), max_length=255)
    slug = models.SlugField(_('Идентификатор ссылки '), unique=True, help_text='Заполняется автоматически по заголовку. В случае неуникальности добавить в конце цифру')
    description = models.TextField(_('Описание'),  blank=True, null=True)
    year = models.IntegerField(_('Год выпуска'))
    tour = models.ForeignKey(Tour, verbose_name=_('Тур в поддержку альбома'), null=True, on_delete=models.SET_NULL)
    album_type = models.IntegerField(_('Тип альбома'), choices=album_types, default=0)
    associated_tags = TaggableManager(verbose_name=_('Ассоциированные теги'))
    buy_links = models.ManyToManyField(BuyLink, verbose_name=_('Ссылки на покупку альбома'))
    tracks = models.ManyToManyField("Track", through="TrackInAlbum", verbose_name=(_("Треки в альбоме")))

    class Meta:
        verbose_name = _('Альбом')
        verbose_name_plural = _('Альбомы')

    def __str__(self):
        return self.name
"""
class AlbumMusician(models.Model):
    album = models.ForeignKey(Album, verbose_name=_('Альбом'))
    musician = models.ForeignKey(Musician, verbose_name=_('Музыкант'))
    comment = models.TextField(_('Дополнительная информация'), blank=True, null=True)

    class Meta:
        verbose_name = _('Музыкант, участвовавший в записи альбома')
        verbose_name_plural = _('Музыкант, участвовавший в записи альбома')

    def __str__(self):
        return self.album + " - " + self.track
"""

class Track(models.Model):
    name = models.CharField(_('Наименование песни'), max_length=255)
    lyrics = models.TextField(_('Текст песни'),  blank=True, null=True)
    duration = models.IntegerField(_('Длительность (сек.)'))
    official_clip_link = models.ForeignKey(VideoLink, verbose_name=_('Официальный клип'), on_delete=models.SET_NULL, null=True)
    buy_links = models.ManyToManyField(BuyLink, verbose_name=_('Ссылки на покупку трека'))

    class Meta:
        verbose_name = _('Трек')
        verbose_name_plural = _('Треки')

    def __str__(self):
        return self.name

class TrackInAlbum(models.Model):
    num = models.IntegerField("№")
    album = models.ForeignKey(Album, verbose_name=_('Альбом'), on_delete=models.CASCADE)
    track = models.ForeignKey(Track, verbose_name=_('Трек'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Трек в альбоме')
        verbose_name_plural = _('Треки в альбоме')

    def __str__(self):
        return self.album + " - " + self.track

class LyricTranslationLang(models.Model):
    lang_tag = models.CharField(_('Язык перевода'), max_length=255)

    class Meta:
        verbose_name = _('Язык перевода')
        verbose_name_plural = _('Языки перевода')

    def __str__(self):
        return self.lang_tag

class LyricsTranslation(models.Model):
    track = models.ForeignKey(Track, verbose_name=_('Трек'), on_delete=models.SET_NULL, null=True)
    lang = models.ForeignKey(LyricTranslationLang, verbose_name=_('Язык перевода'), on_delete=models.SET_NULL, null=True)
    text = models.TextField(_('Текст перевода'))
    author = models.CharField(_('Автор перевода'), max_length=255)
    lotl_team = models.ForeignKey(LotlTeamMember, _('Участник команды LOTL-info'), blank=True, null=True)

    class Meta:
        verbose_name = _('Трек в альбоме')
        verbose_name_plural = _('Треки в альбоме')

    def __str__(self):
        return self.track + " (" + self.lang + ")"

class Event(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255)
    slug = models.SlugField(_('Идентификатор ссылки '), unique=True, help_text='Заполняется автоматически по заголовку. В случае неуникальности добавить в конце цифру')
    anons = models.TextField(_('Анонс'), blank=True, null=True)
    dt = models.DateField(_('Дата события'))
    tour = models.ForeignKey(Tour, verbose_name=_('Тур'), on_delete=models.SET_NULL, null=True)
    country = models.CharField(_('Страна'), max_length=255)
    city  = models.CharField(_('Город (местность)'), max_length=255)
    club = models.CharField(_('Клуб'), max_length=255, blank=True, null=True)
    is_published = models.BooleanField(_('Опубликовано'), default=False)
    tags = TaggableManager(verbose_name=_('Теги'),  blank=True)
    vk_album = models.URLField(_('Альбом ВК'), null=True, blank=True)
    videos = models.ManyToManyField(VideoLink, verbose_name=_('Видео к событию'))
    tickets = models.ManyToManyField(BuyLink, verbose_name=_('Ссылки на покупку билетов'))
    news = models.ManyToManyField('News', verbose_name=_('Новости по событию'))
    articles = models.ManyToManyField('Article', verbose_name=_('Статьи по событию'))
    photos = models.ManyToManyField(Photo, verbose_name=_('Фото к материалу'), through='PhotoEvent')

    class Meta:
        verbose_name = _('Событие')
        verbose_name_plural = _('События')

    def __str__(self):
        return self.title

class TextMaterial(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255)
    slug = models.SlugField(_('Идентификатор ссылки '), unique=True, help_text='Заполняется автоматически по заголовку. В случае неуникальности добавить в конце цифру')
    text_short = models.TextField(_('Анонс'))
    text_full = models.TextField(_('Текст'))
    dt_created = models.DateTimeField(_('Дата создания'), auto_now_add=True)
    proof_link = models.URLField(_('Пруф'), help_text=_('Ссылка на пруф или оригинальный источник'), blank=True, null=True)
    is_published = models.BooleanField(_('Опубликовано'), default=False)
    vk_album = models.URLField(_('Альбом ВК'), null=True, blank=True)
    translator = models.ForeignKey(LotlTeamMember, verbose_name=_('Переводчик'), null=True, on_delete=models.SET_NULL, blank=True)
    tags = TaggableManager(verbose_name=_('Теги'),  blank=True)
    videos = models.ManyToManyField(VideoLink, verbose_name=_('Видео к материалу'), blank=True, null=True)
    photos = models.ManyToManyField(Photo, verbose_name=_('Фото к материалу'),  through='PhotoText')

class News(TextMaterial):
    news_types = ((0,_('Другой')),(1, _('Новости группы')), (2,_('Новости соо')))
    news_type = models.IntegerField(_('Тип новости'), choices=news_types, default=0)

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')

    def __str__(self):
        return self.title

class Article(TextMaterial):
    article_types = ((0,_('Другой')),(1, _('Статья')), (2,_('Интервью')),(3, _('Мифилогия')), (4, _('Отчет')))
    article_type = models.IntegerField(_('Тип статьи'), choices=article_types, default=0)
    author = models.CharField(_('Автор'), blank=True, null=True, max_length=255)
    author_link = models.URLField(_('Ссылка на автора'), blank=True, null=True)

    class Meta:
        verbose_name = _('Статья')
        verbose_name_plural = _('Статьи')

    def __str__(self):
        return self.title

class PhotoEvent(models.Model):
    event = models.ForeignKey(Event, verbose_name=_('Событие'), on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, verbose_name=_('Фотография с события'), on_delete=models.CASCADE)
    is_cover = models.BooleanField(_('Обложка'), default=False)

    class Meta:
        verbose_name = _('Фотография с события')
        verbose_name_plural = _('Фотографии с события')

    def __str__(self):
        return self.event + ' ' + self.photo

class PhotoText(models.Model):
    text_material = models.ForeignKey(TextMaterial, verbose_name=_('Событие'), on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, verbose_name=_('Фотография к тексту'), on_delete=models.CASCADE)
    is_cover = models.BooleanField(_('Обложка'), default=False)

    class Meta:
        verbose_name = _('Фотография к тексту')
        verbose_name_plural = _('Фотографии к тексту')

    def __str__(self):
        return self.text_material + ' ' + self.photo