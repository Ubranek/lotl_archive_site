from django.urls import path

from . import views

urlpatterns = [
    #http://localhost:8000/tests/translate_list/
    path('translate_list/', views.translation_page, name='translation_page'),
]