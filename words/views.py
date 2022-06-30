from django.http import HttpResponse
from django.shortcuts import render
from . import models


def index(request):
    word_list = models.Word.objects.all()
    return render(request, "words/index.html", locals())


def index_temp(request):
    word_list = models.Word.objects.all()
    return render(request, "words/index_temp.html", locals())