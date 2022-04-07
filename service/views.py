from audioop import reverse
from tempfile import template
from django.http import HttpResponse, Http404, FileResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Product
from django.template.loader import get_template
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request, id):
    try:
        var = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404('NOT FOUND!')
    return HttpResponse('OK')

def json_show(req):
    data = {'cost':14, 'title':'book'}
    return JsonResponse(data)