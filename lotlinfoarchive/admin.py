from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

# Register your models here.

class TextInfoBlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'template_name')
    list_editable = ('template_name',)


class BuyLinkTicketsInline(admin.StackedInline):
    model = Event.tickets.through
    classes = ['collapse']
    extra = 1

class BuyLinkAlbumInline(admin.StackedInline):
    model = Album.buy_links.through
    classes = ['collapse']
    extra = 1

class BuyLinkTrackInline(admin.StackedInline):
    model = Track.buy_links.through
    classes = ['collapse']
    extra = 1

class PhotoInline(admin.StackedInline):
    model = Photo
    classes = ['collapse']
    extra = 1

class MusicianPhotoInline(admin.StackedInline):
    model = Musician.photo.through
    classes = ['collapse']
    extra = 1

class MusicianAdmin(SummernoteModelAdmin):
    model = Musician
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'associated_tags',)
    list_editable = ('associated_tags',)
    inlines = [
        MusicianPhotoInline,
    ]
    summernote_fields = ('info', 'info_en', 'info_de',)

    fieldsets = (
        (None, {
            'fields': ('name', 'real_name', 'role', 'facebook', 'instagram', 'info', 'is_active', 'associated_tags', 'signature')
        }),
        ('Перевод ENGLISH', {
            'classes': ('collapse',),
            'fields': ('role_en', 'info_en', )
        }),
        ('Перевод DEUTSCH', {
            'classes': ('collapse',),
            'fields': ('role_de', 'info_de', )
        }),
        ('СЛУЖЕБНЫЕ ( Читаемая ссылка, пр', {
            'classes': ('collapse',),
            'fields': ('slug', ),
        }),
    )

class TrackInAlbumInline(admin.StackedInline):
    model = Album.tracks.through
    classes = ['collapse']
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
    model = Album
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        BuyLinkAlbumInline, TrackInAlbumInline,
    ]


class TrackAdmin(admin.ModelAdmin):
    model = Track
    inlines = [
        BuyLinkTrackInline,
    ]

"""
class PhotoEventInline(admin.StackedInline):
    model = Event.photos.through
    classes = ['collapse']
    extra = 1

class PhotoTextInline(admin.StackedInline):
    model = TextMaterial.photos.through
    classes = ['collapse']
    extra = 1

class VideoLinkEventInline(admin.StackedInline):
    model = Event.videos.through
    classes = ['collapse']
    extra = 1
"""

class EventAdmin(SummernoteModelAdmin):
    model = Event
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'dt', 'tags', 'is_published', )
    list_editable = ('tags', 'is_published',)
    #inlines = [
       # BuyLinkTicketsInline, PhotoEventInline, VideoLinkEventInline
    #]
    filter_horizontal = ('news', 'articles', 'videos', 'site_photos')
    summernote_fields = '__all__'
    fieldsets = (
        (None, {
            'fields': ('title', 'anons', 'dt',)
        }),
        ('Перевод ENGLISH', {
            'classes': ('collapse',),
            'fields': ('title_en', 'anons_en', )
        }),
        ('Перевод DEUTSCH', {
            'classes': ('collapse',),
            'fields': ('title_de', 'anons_de', )
        }),
        ('Параметры оформленния', {
            'classes': ('collapse',),
            'fields': ('cover',  'vk_album', 'tags', 'is_published',)
        }),
        ('Место проведения', {
            'classes': ('collapse',),
            'fields': ('tour', 'country', 'city', 'club',)
        }),
        ('Перекрестные ссылки на сайте (не поиск по тегам)', {
            'classes': ('collapse',),
            'fields': (  'tickets', 'news', 'articles',  'videos', 'site_photos',)
        }),
        ('СЛУЖЕБНЫЕ ( Читаемая ссылка, пр', {
            'classes': ('collapse',),
            'fields': ('slug', ),
        }),
    )

"""
class EventNewsInline(admin.StackedInline):
    model = Event.news.through
    classes = ['collapse']
    extra = 1

class VideoLinkNewsInline(admin.StackedInline):
    model = News.videos.through
    classes = ['collapse']
    extra = 1
"""

class NewsAdmin(SummernoteModelAdmin):
    model = News
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'dt_created', 'is_published', 'tags')
    list_editable = ('is_published', 'tags',)
    filter_horizontal = ('videos_urls', 'site_photos',)
    fieldsets = (
        (None, {
            'fields': ('title', 'text_short', 'text_full', 'cover', 'is_published', 'tags')
        }),
        ('Перевод ENGLISH', {
            'classes': ('collapse',),
            'fields': ('title_en', 'text_short_en', 'text_full_en' )
        }),
        ('Перевод DEUTSCH', {
            'classes': ('collapse',),
            'fields': ('title_de', 'text_short_de', 'text_full_de')
        }),
        ('Перекрестные ссылки на сайте (не поиск по тегам)', {
            'classes': ('collapse',),
            'fields': ( 'videos_urls', 'site_photos',)
        }),
        ('СЛУЖЕБНЫЕ (Переводчик, Читаемая ссылка, пр', {
            'classes': ('collapse',),
            'fields': ('translator', 'slug',),
        }),
    )
    """
    inlines = [
         VideoLinkNewsInline, EventNewsInline
    ]
    """
    summernote_fields = '__all__'

"""
class VideoLinkArticleInline(admin.StackedInline):
    model = News.videos.through
    classes = ['collapse']
    extra = 1
"""

class ArticleAdmin(SummernoteModelAdmin):
    model =  Article
    prepopulated_fields = {'slug': ('title',), }
    list_display = ('title', 'dt_created', 'is_published', 'tags')
    list_editable = ('is_published', 'tags',)
    filter_horizontal = ('videos_urls', 'site_photos',)
    #fields = ('tags',)

    fieldsets = (
        (None, {
            'fields': ('title', 'text_short', 'text_full', 'cover', 'article_type', 'author', 'author_link', 'tags', 'is_published')
        }),
        ('Перевод ENGLISH', {
            'classes': ('collapse',),
            'fields': ('title_en', 'text_short_en', 'text_full_en')
        }),
        ('Перевод DEUTSCH', {
            'classes': ('collapse',),
            'fields': ('title_de', 'text_short_de', 'text_full_de')
        }),
        ('Перекрестные ссылки на сайте (не поиск по тегам)', {
            'classes': ('collapse',),
            'fields': ('videos_urls', 'site_photos',)
        }),
        ('СЛУЖЕБНЫЕ (Переводчик, Читаемая ссылка, пр', {
            'classes': ('collapse',),
            'fields': ('translator', 'slug',),
        }),
    )
    """
    inlines = [
        VideoLinkArticleInline, PhotoTextInline,
    ]
    """
    summernote_fields = '__all__'

admin.site.register(TextInfoBlock, TextInfoBlockAdmin)
admin.site.register(LotlTeamMember)
admin.site.register(Tour)
admin.site.register(Musician, MusicianAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)


admin.site.register(LyricsTranslation)
admin.site.register(LyricTranslationLang)
admin.site.register(Event, EventAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(VideoLink)
admin.site.register(Photo)
admin.site.register(BuyLink)

