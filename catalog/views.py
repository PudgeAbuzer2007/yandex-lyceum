from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, num):
    return HttpResponse("<body>	Подробно элемент</body>")
