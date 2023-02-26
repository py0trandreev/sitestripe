from django.urls import path
from .views import (
    CheckoutSessionView,
    ProductPageView,
    ProductListView,
    SuccessView,
    CancelView,
)

app_name = "products"

urlpatterns = [
    path("item/<int:item_id>/", ProductPageView.as_view(), name="item"),
    path("items/", ProductListView.as_view(), name="items"),
    path("success/", SuccessView.as_view(), name="success"),
    path("cancel/", CancelView.as_view(), name="cancel"),
    path("buy/<pk>/", CheckoutSessionView.as_view(), name="buy"),
]
