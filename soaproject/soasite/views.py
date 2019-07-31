from django.http import HttpResponse
from django.template import loader
from django.core import serializers
from .models import Bookmark
from django.http import JsonResponse


def index(request):
    template = loader.get_template('soasite/index.html')
    return HttpResponse(template.render(None, request))

def bookmark(request):
    arrayData = []
    for values in Bookmark.objects.values():
        arrayData.append(values)

    data = {"data": arrayData}
    return JsonResponse(data, safe=False)
