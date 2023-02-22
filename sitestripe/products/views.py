from django.http import HttpResponse
from django.shortcuts import render

def item(request, item_id):
    return HttpResponse(f"<h1>Items </h1> <p>{item_id}</p>")
