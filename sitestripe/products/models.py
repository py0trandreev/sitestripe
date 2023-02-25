from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    price = models.IntegerField(default=0)  # cents, kopecks

    def __str__(self):
        return self.name

    def get_display_price(self):
        return f"{self.price / 100:.2f}"
