from django.db import models
from django.shortcuts import render, resolve_url
from django.http.response import JsonResponse
from quote.models import Product

# ! INVENTORY VIEWS
def home(request):

    return render(request, "inventory/index.html")


def get_inventory_index(request):

    products = Product.objects.all()

    return JsonResponse([product.serialize() for product in products], safe=False)


def new_product_form(request):
    return render(request, 'inventory/create-product.html')