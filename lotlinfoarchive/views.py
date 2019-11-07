from django.shortcuts import render_to_response
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
        context['text_info'] = TextInfoBlock.objects.get_or_create(template_name=self.template_name)[0]
        context['menu'] = get_menu()
        #context['latest_articles'] = Article.objects.all()[:5]
        return context

#path('news/', NewsView, "lotlarchive.news"),
class NewsView(ListView):
    model = News
    paginate_by = 10
    template_name = "lotlinfoarchive/news_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text_info'] = TextInfoBlock.objects.get_or_create(template_name=self.template_name)[0]
        context['menu'] = get_menu()
        return context

#path('news/<slug:slug>', SingleNewsView, "lotlarchive.single_news"),
class SingleNewsView(DetailView):
    model = News
    template_name = "lotlinfoarchive/news_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context


# path('articles/', ArticlesView, "lotlarchive.articles"),
class ArticlesView(ListView):
    model = Article
    paginate_by = 10
    template_name = "lotlinfoarchive/article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text_info'] = TextInfoBlock.objects.get_or_create(template_name=self.template_name)[0]
        context['menu'] = get_menu()
        return context


# path('articles/<slug:slug>', SingleArticlesView, "lotlarchive.single_article"),
class SingleArticlesView(DetailView):
    model = Article
    template_name = "lotlinfoarchive/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context

#path('about/', AboutView, "lotlarchive.about"),
class AboutView(TemplateView):
    template_name = "lotlinfoarchive/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text_info'] = TextInfoBlock.objects.get_or_create(template_name=self.template_name)[0]
        context['menu'] = get_menu()
        return context

#path('discography/', DiscographyView, "lotlarchive.discography"),
class DiscographyView(ListView):
    model = Album

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text_info'] = TextInfoBlock.objects.get_or_create(template_name=self.template_name)[0]
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

#path('tours/<slug:slug>', TourView.as_view(), name='lotlarchive.tour'),
class TourView(DetailView):
    model = Tour

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["events"] = Event.objects.filter(tour=self.object)
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

#path('photo/<int:id>', SinglePhoto.as_view(), name="lotlarchive.single_photo"),
class SinglePhotoView(DetailView):
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

#path('musisians/', MusiciansView, "lotlarchive.musisians"),
class MusiciansView(ListView):
    model = Musician

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text_info'] = TextInfoBlock.objects.get_or_create(template_name=self.template_name)[0]
        context['menu'] = get_menu()
        return context

#path('musisians/<slug:slug>', SingleMusicianView, "lotlarchive.musician"),
class SingleMusicianView(DetailView):
    model = Musician

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = get_menu()
        return context


def tag_search(request, tag):
    template_name = "lotlinfoarchive/tag_search_result.html"

    events = Event.objects.filter(tags__slug__in=[tag,])
    text_list = []
    news_list = News.objects.filter(tags__slug__in=[tag,])
    article_list = Article.objects.filter(tags__slug__in=[tag,])
    text_list = list(news_list) + list(article_list)
    videos = VideoLink.objects.filter(tags__slug__in=[tag,])
    photoes = Photo.objects.filter(tags__slug__in=[tag,])

    tours = Tour.objects.filter(associated_tags__slug__in=[tag,])
    musicians = Musician.objects.filter(associated_tags__slug__in=[tag,])
    albums = Album.objects.filter(associated_tags__slug__in=[tag, ])

    context = {}
    context['menu'] = get_menu()
    context["tag"] = tag

    context["events"] = events
    context["text_list"] = text_list
    context["videos"] = videos
    context["photoes"] = photoes
    context["tours"] = tours
    context["musicians"] = musicians
    context['albums'] = albums

    return render_to_response(template_name, context)




