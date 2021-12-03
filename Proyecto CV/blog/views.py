from django.shortcuts import render
from .models import Curriculum


def cv_view(request):
    cv = Curriculum.objects.get(nombre_completo="Christian Silva")
    return render(request, 'blog/cv_view.html', {"cv":cv})