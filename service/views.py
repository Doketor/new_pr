from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404

from django.core.exceptions import ObjectDoesNotExist

from .models import Product

def index(request):
    return HttpResponse('Hello, World!')

def about(request, id):
    try:
        var = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        raise Http404('NOT FOUND!')
    return HttpResponse('OK')