'''
главная (1)
новости (2)
абоут (3)
дискография (4)
ивенты (5)
фото (6)
видео (7)
статьи (8)
о нас (9) (статичная страничка)
'''

from django.urls import include, path
from .views import *

urlpatterns = [
    path('', MainView.as_view(), name="lotlarchive.main"),
    path('news/', NewsView.as_view(), name="lotlarchive.news"),
    path('news/<slug:slug>/', SingleNewsView.as_view(), name="lotlarchive.single_news"),
    path('articles/', ArticlesView.as_view(), name="lotlarchive.articles"),
    path('articles/<slug:slug>/', SingleArticlesView.as_view(), name="lotlarchive.single_article"),
    path('about/', AboutView.as_view(), name= "lotlarchive.about"),
    path('discography/', DiscographyView.as_view(), name="lotlarchive.discography"),
    path('discography/<slug:slug>', AlbumView.as_view(), name="lotlarchive.album"),
    path('events/', EventsView.as_view(), name="lotlarchive.events"),
    path('events/<slug:slug>', SingleEventView.as_view(), name="lotlarchive.single_event"),
    path('tours/<slug:slug>', TourView.as_view(), name="lotlarchive.tour"),
    #path('archive/', ArchiveView.as_view(), name="lotlarchive.archive"),
    path('photos/', PhotoesView.as_view(), name="lotlarchive.photoes"),
    path('photo/<int:pk>', SinglePhotoView.as_view(), name="lotlarchive.single_photo"),
    path('videos/', VideosView.as_view(), name="lotlarchive.videos"),
    path('musisians/', MusiciansView.as_view(), name="lotlarchive.musisians"),
    path('musisians/<slug:slug>', SingleMusicianView.as_view(), name="lotlarchive.musician"),

    path('tags/<str:tag>', tag_search, name="lotlarchive.tags_list")
]

'''
    
    path('about/', AboutView, "lotlarchive.main"),
    path('discography/', DiscographyView, "lotlarchive.main"),
    path('events/', EventsView, "lotlarchive.main"),
    path('photos/', PhotoesView, "lotlarchive.main"),
    path('videos/', VideosView, "lotlarchive.main"),
    path('articles/', ArticlesView, "lotlarchive.main"),
    path('musisians/', MusiciansView, "lotlarchive.main"),
'''
