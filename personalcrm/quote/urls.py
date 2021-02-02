from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="quote-home"),
    path("create-quote", views.create_quote, name="create-quote"),
    path("edit-quote/<int:quote_id>", views.edit_quote, name="edit-quote"),
    # JSON routes
    path(
        "request-product-options",
        views.get_product_options,
        name="request-product-options",
    ),
    path(
        "product/<str:pn>",
        views.get_product_info,
        name="product-info",
    ),
    path("quote-index", views.get_quote_index, name="quote-index"),
]
