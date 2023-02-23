from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def item(request, item_id):
    item = Item.objects.get(pk=item_id)

    return render(request, "products/item.html", {"item": item})
