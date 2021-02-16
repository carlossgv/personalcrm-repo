from .forms import NewProductForm
from django.db import models
from django.shortcuts import render, resolve_url
from django.http.response import JsonResponse
from quote.models import Product, Brand, User

# ! INVENTORY VIEWS
def home(request):

    return render(request, "inventory/index.html")


def get_inventory_index(request):

    products = Product.objects.all()

    return JsonResponse([product.serialize() for product in products], safe=False)


def new_product_form(request):

    if request.method == "POST":

        form = NewProductForm(request.POST)

        user = request.user

        if form.is_valid():
            creator = User.objects.get(username=user)
            pn = form.cleaned_data["pn"]
            brand = Brand.objects.get(pk=form.cleaned_data["brand"])
            print(form.cleaned_data)
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            list_price = form.cleaned_data["list_price"]
            multiplier = form.cleaned_data["multiplier"]
            stock = form.cleaned_data["stock"]
            note = form.cleaned_data["note"]

            product = Product(
                pn=pn,
                brand=brand,
                title=title,
                description=description,
                creator = creator,
                list_price=list_price,
                multiplier=multiplier,
                stock=stock,
                note=note,
            )

            product.save()

        return render(request, "inventory/create-product.html", {"form": form})

    else:
        form = NewProductForm()

        return render(request, "inventory/create-product.html", {"form": form})
