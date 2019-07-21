from django.contrib import admin
from .models import *

# Register your models here.
class BuyLinkTicketsInline(admin.StackedInline):
    model = Event.tickets.through

class BuyLinkAlbumInline(admin.StackedInline):
    model = Album.buy_links.through

class BuyLinkTrackInline(admin.StackedInline):
    model = Track.buy_links.through

class PhotoInline(admin.StackedInline):
    model = Photo

class MusicianPhotoInline(admin.StackedInline):
    model = Musician.photo.through

class MusicianAdmin(admin.ModelAdmin):
    model = Musician
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        MusicianPhotoInline,
    ]

class TrackInAlbumInline(admin.StackedInline):
    model = Album.tracks.through

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

class PhotoEventInline(admin.StackedInline):
    model = Event.photos.through

class PhotoTextInline(admin.StackedInline):
    model = TextMaterial.photos.through

class VideoLinkEventInline(admin.StackedInline):
    model = Event.videos.through

class EventAdmin(admin.ModelAdmin):
    model = Event
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        VideoLinkEventInline, BuyLinkTicketsInline, PhotoEventInline,
    ]

class VideoLinkNewsInline(admin.StackedInline):
    model = News.videos.through

class NewsAdmin(admin.ModelAdmin):
    model = News
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        VideoLinkNewsInline, PhotoTextInline,
    ]

class VideoLinkArticleInline(admin.StackedInline):
    model = News.videos.through

class ArticleAdmin(admin.ModelAdmin):
    model =  Article
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        VideoLinkArticleInline, PhotoTextInline,
    ]

admin.site.register(LotlTeamMember)
admin.site.register(Tour)
admin.site.register(Musician, MusicianAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)
#admin.site.register(LyricTranslationLang)

admin.site.register(LyricsTranslation)
admin.site.register(Event, EventAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Article, ArticleAdmin)
#admin.site.register(VideoLink, VideoLinkArticleInline)
#admin.site.register(VideoLink, VideoLinkEventInline)
#admin.site.register(VideoLink, VideoLinkNewsInline)