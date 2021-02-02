from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Product, User, Company, Contact, Quote, QuotedProduct
from .utils import create_or_edit_quote, form_options

# Create your views here.
def home(request):

    return render(request, "quote/quote_index.html")


# TODO !! MAJOR CHANGE: IMPLEMENT DJANGO FORMS INSTEAD OF HTML FORMS


def edit_quote(request, quote_id):
    if request.method == "GET":

        data = form_options()

        quote = Quote.objects.get(pk=quote_id)
        products = QuotedProduct.objects.filter(quote=quote)

        return render(
            request,
            "quote/edit-quote.html",
            {
                "company_options": data["company_options"],
                "contact_options": data["contact_options"],
                "product_options": data["product_options"],
                "quote": quote,
                "products": products,
            },
        )

    elif request.method == "POST":
        # user = request.user
        # TODO CHANGE USER TO CURRENT USER OR SELECT USER
        user = User.objects.get(pk=1)
        data = request.POST

        create_or_edit_quote(data, user, "edit", quote_id)

        return HttpResponseRedirect(
            reverse("edit-quote", kwargs={"quote_id": quote_id})
        )


def create_quote(request):
    if request.method == "GET":

        data = form_options()

        return render(
            request,
            "quote/create-quote.html",
            {
                "company_options": data["company_options"],
                "contact_options": data["contact_options"],
                "product_options": data["product_options"],
            },
        )

    elif request.method == "POST":
        data = request.POST

        # user = request.user
        # TODO CHANGE USER TO CURRENT USER OR SELECT USER
        user = User.objects.get(pk=1)

        create_or_edit_quote(data, user, "create")

        return HttpResponseRedirect(reverse("create-quote"))


def request_product_options(request):
    product_options = Product.objects.all().values("pn")
    product_options = [d["pn"] for d in product_options]

    return JsonResponse({"product_options": product_options})


def get_product_info(request, pn):
    product = Product.objects.get(pn=pn)

    return JsonResponse(product.serialize(), safe=False)
