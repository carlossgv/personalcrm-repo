from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Product, User, Company, Contact, Quote, QuotedProduct, UserCompany
from .utils import create_or_edit_quote, form_options

# Create your views here.
def home(request):

    return render(request, "quote/index.html")


# TODO !! MAJOR CHANGE: IMPLEMENT DJANGO FORMS INSTEAD OF HTML FORMS

def login(request):

    return HttpResponseRedirect(reverse("admin:index"))


def view_quote(request, quote_id):
    quote = Quote.objects.get(pk=quote_id)
    products = QuotedProduct.objects.filter(quote=quote)
    # TODO Pass selected logo (not hardcoded)
    logo = "img"
    company = UserCompany.objects.get(pk=1)



    return render(
        request,
        "quote/view-quote.html",
        {"quote": quote, "products": [product.serialize() for product in products], "company": company},
    )


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
        edit = create_or_edit_quote(data, user, "edit", quote_id)

        print(edit)

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

        create = create_or_edit_quote(data, user, "create")
        print(create)
        return HttpResponseRedirect(reverse("quote-home"))


def get_product_options(request):

    product_options = Product.objects.all().values("pn")
    product_options = [d["pn"] for d in product_options]

    return JsonResponse({"product_options": product_options})


def get_product_info(request, pn):

    product = Product.objects.get(pn=pn)

    return JsonResponse(product.serialize(), safe=False)


def get_quote_index(request):

    quotes = Quote.objects.all()

    return JsonResponse([quote.serialize() for quote in quotes], safe=False)

def get_quote_products(request, quote_id):

    products = QuotedProduct.objects.filter(quote = Quote.objects.get(pk=quote_id))

    return JsonResponse([product.serialize() for product in products], safe=False)