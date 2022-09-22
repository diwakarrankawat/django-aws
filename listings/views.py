from time import time
from rest_framework.generics import ListAPIView, GenericAPIView, ListCreateAPIView
from django.http.response import HttpResponse

from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework.response import Response

# locals
from . import models


def home(request):
    page = models.Page()
    page.path = ''
    page.title = 'Home Page'
    page.keywords = 'keywords1, keyword2, keyword3'
    page.description = "A description about our page"
    return render(request, 'index.html', {"page": page})


def flutter(request, page):
    ng = models.Page.objects.filter(path=page)
    if ng.exists():
        page = ng.first()
    else:
        page = models.Page()
        page.title = 'Inncar Web'
    return render(request, "index.html", {"page": page})
