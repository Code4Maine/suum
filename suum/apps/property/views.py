from django.shortcuts import render

from .models import Property
# Create your views here.

def homepage(request):
    objects = []

    for p in Property.objects.all():
        if p.property_delta:
            objects.append(p)

    return render(request, 'homepage.html', {'objects': objects})
