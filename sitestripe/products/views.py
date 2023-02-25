import stripe
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import DetailView, TemplateView
from django.shortcuts import render
from .models import *

stripe.api_key = settings.STRIPE_SECRET_KEY


def item(request, item_id):
    item = Item.objects.get(pk=item_id)

    return render(request, "products/item.html", {"item": item})


class ProductPageView(DetailView):
    model = Item
    template_name = "products/product.html"
    pk_url_kwarg = "item_id"
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super(ProductPageView, self).get_context_data(**kwargs)
        context.update(
            {
                "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
            }
        )
        return context


class CheckoutSessionView(View):
    def get_session_id(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = Item.objects.get(pk=product_id)

        # create stripe product
        product_json = stripe.Product.create(
            name=product.name, description=product.description
        )
        product_stripe_id = product_json.id

        # create stripe price
        price_json = stripe.Price.create(
            unit_amount=product.price,
            currency="usd",  # in cents
            product=product_stripe_id,
        )
        price_stripe_id = price_json.id

        MAIN_DOMAIN = "http://127.0.0.1:8000/products"

        checkout_session_json = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": price_stripe_id,
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url=MAIN_DOMAIN + "/success/",
            cancel_url=MAIN_DOMAIN + "/cancel/",
        )

        return checkout_session_json.id

    def post(self, request, *args, **kwargs):
        return JsonResponse({"id": self.get_session_id(self, request, *args, **kwargs)})

    def get(self, request, *args, **kwargs):
        return JsonResponse({"id": self.get_session_id(self, request, *args, **kwargs)})


class SuccessView(TemplateView):
    template_name = "products/success.html"


class CancelView(TemplateView):
    template_name = "products/cancel.html"
