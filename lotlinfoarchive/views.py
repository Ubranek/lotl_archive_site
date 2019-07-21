from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import *

# Create your views here.


#вспомогательные функции
def get_menu():
    class MenuItem:
        url = ""
        title = ""
        level = 1
        def __init__(self, url, title, level=1):
            self.url = url
            self.title = title
            self.level = level


    menu = [MenuItem(reverse('lotlarchive.main'), "Главная"),
            MenuItem(reverse('lotlarchive.news'), "Новости"),
            MenuItem(reverse('lotlarchive.discography'), "Дискография"),
            MenuItem(reverse('lotlarchive.musisians'), "О группе"),
            MenuItem(reverse('lotlarchive.events'), "События"),
            #MenuItem(reverse('lotlarchive.archive'), "Архив материалов"),
            MenuItem(reverse('lotlarchive.photoes'), "Фото", 2),
            MenuItem(reverse('lotlarchive.videos'), "Видео", 2),
            MenuItem(reverse('lotlarchive.articles'), "Статьи", 2),
            MenuItem(reverse('lotlarchive.about'), "О нас")]

    return menu

#основные классы-отображения
#path('/', MainView, "lotlarchive.main"),
class MainView(TemplateView):
    template_name = "lotlinfoarchive/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        #context['latest_articles'] = Article.objects.all()[:5]
        return context

#path('news/', NewsView, "lotlarchive.news"),
class NewsView(ListView):
    model = News
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context

#path('news/<slug:slug>', SingleNewsView, "lotlarchive.single_news"),
class SingleNewsView(DetailView):
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context

#path('about/', AboutView, "lotlarchive.about"),
class AboutView(TemplateView):
    template_name = "lotlinfoarchive/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context

#path('discography/', DiscographyView, "lotlarchive.discography"),
class DiscographyView(ListView):
    model = Album

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context

#path('discography/album/<slug:slug>', AlbumView, "lotlarchive.album"),
class AlbumView(DetailView):
    model = Album

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context

#path('events/', EventsView, "lotlarchive.events"),
class EventsView(ListView):
    model = Event
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context

#path('events/<slug:slug>', SingleEventView, "lotlarchive.single_event"),
class SingleEventView(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context

#path('photos/', PhotoesView, "lotlarchive.photoes"),
class PhotoesView(ListView):
    model = Photo
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context

#path('videos/', VideosView, "lotlarchive.videos"),
class VideosView(ListView):
    model = VideoLink
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context

#path('articles/', ArticlesView, "lotlarchive.articles"),
class ArticlesView(ListView):
    model = Article
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context

#path('articles/<slug:slug>', SingleArticlesView, "lotlarchive.single_article"),
class SingleArticlesView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context

#path('musisians/', MusiciansView, "lotlarchive.musisians"),
class MusiciansView(ListView):
    model = Musician

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context

#path('musisians/<slug:slug>', SingleMusicianView, "lotlarchive.musician"),
class SingleMusicianView(DetailView):
    model = Musician

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context