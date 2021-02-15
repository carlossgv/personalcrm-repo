from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="inventory-home"),
    path("create-product", views.new_product_form, name="create-product"),
    # Json Paths
    path("inventory-index", views.get_inventory_index, name="inventory-index"),
]