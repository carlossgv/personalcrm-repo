from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Product, User, Company, Contact
from .utils import createProduct, createCompany, createQuote

# Create your views here.
def home(request):

    return render(request, "quote/quote_index.html")


def create_quote(request):

    if request.method == "GET":

        company_options = Company.objects.all().values_list("name", flat=True)

        product_options = []

        products = Product.objects.all().values_list("pn", "title")
        for product in products:
            product_options.append(f"{product[0]}: {product[1]}")

        return render(
            request,
            "quote/create-quote.html",
            {"company_options": company_options, "product_options": product_options},
        )
    elif request.method == "POST":

        print(request.POST)

        return HttpResponseRedirect(reverse("create-quote"))


def request_product_options(request):

    product_options = Product.objects.all().values("pn")
    product_options = [d["pn"] for d in product_options]

    return JsonResponse({"product_options": product_options})


def get_product_info(request, pn):

    product = Product.objects.get(pn=pn)

    return JsonResponse(product.serialize(), safe=False)
