from django.urls import path, include

from .models import SimpleTranslationModel
from . import views

urlpatterns = [
    #http://localhost:8000/tests/translate_list/
    path('translate_list/', views.translation_page, name='translation_page'),
   # path('^widgets/tag/(?P<tag>[^/]+(?u))/',
  #      TaggedObjectList.as_view(model=SimpleTranslationModel, paginate_by=10, allow_empty=True),
  #      name='widget_tag_detail'),
]

