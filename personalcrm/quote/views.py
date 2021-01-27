from django.shortcuts import render
from .models import Product, User, Company, Contact
from .utils import createProduct, createCompany, createQuote

# Create your views here.
def home(request):

    return render(request, "quote/quote_index.html")


def create_quote(request):

    company_options = Company.objects.all().values("name")
    company_options = [d["name"] for d in company_options]

    product_options = Product.objects.all().values("pn")
    product_options = [d["pn"] for d in product_options]

    return render(
        request,
        "quote/create-quote.html",
        {"company_options": company_options, "product_options": product_options},
    )
