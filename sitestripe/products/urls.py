from django.urls import path
from .views import *

urlpatterns = [
    path("item/<int:item_id>/", item)
]