from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Product, User, Company, Contact, Quote, QuotedProduct
from .utils import create_or_edit_quote

# Create your views here.
def home(request):

    return render(request, "quote/quote_index.html")


# TODO !! MAJOR CHANGE: IMPLEMENT DJANGO FORMS INSTEAD OF HTML FORMS


def edit_quote(request, quote_id):
    print("ENTERED EDIT GET")
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
        print("ENTERED POST EDIT")
        # user = request.user
        # TODO CHANGE USER TO CURRENT USER OR SELECT USER
        user = User.objects.get(pk=1)
        data = request.POST
        edit = create_or_edit_quote(data, user, "edit", quote_id)

        print(edit)

        return HttpResponseRedirect(reverse("edit-quote", kwargs={'quote_id': quote_id}))


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
        print("ENTERED POST CREATE")

        data = request.POST

        # user = request.user
        # TODO CHANGE USER TO CURRENT USER OR SELECT USER
        user = User.objects.get(pk=1)

        create = create_or_edit_quote(data, user, "create")
        print(create)
        return HttpResponseRedirect(reverse("create-quote"))


def request_product_options(request):

    product_options = Product.objects.all().values("pn")
    product_options = [d["pn"] for d in product_options]

    return JsonResponse({"product_options": product_options})


def get_product_info(request, pn):

    product = Product.objects.get(pn=pn)

    return JsonResponse(product.serialize(), safe=False)


def form_options():
    company_options = []
    companies = Company.objects.all()
    for company in companies:
        company_options.append({"id": company.id, "info": company.name})

    contact_options = []
    contacts = Contact.objects.all()
    for contact in contacts:
        contact_options.append(
            {
                "id": contact.id,
                "info": f"{contact.first_name} {contact.last_name} | {contact.company.name} | {contact.email}",
            }
        )

    product_options = []
    products_list = Product.objects.all()
    for product in products_list:
        product_options.append(
            {"id": product.id, "info": f"{product.pn}: {product.title}"}
        )

    return {
        "company_options": company_options,
        "contact_options": contact_options,
        "product_options": product_options,
    }
