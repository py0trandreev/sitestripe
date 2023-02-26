from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    price = models.IntegerField(default=0, verbose_name="Price (in cents)")  # cents

    def __str__(self):
        return self.name

    def get_display_price(self):
        return f"{self.price / 100:.2f}"

    def get_absolute_url(self):
        return reverse("products:item", kwargs={"item_id": self.pk})
