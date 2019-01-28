from django.http import HttpResponse
from .models import SimpleTranslationModel
from django.shortcuts import get_object_or_404, render

def translation_page(request):
    template_name = 'translation_page.html'
    entity_list = SimpleTranslationModel.objects.all()
    context = {}
    context['translate_entities'] = entity_list
    print(request.LANGUAGE_CODE)
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, template_name, context)