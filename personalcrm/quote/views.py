from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Product, User, Company, Contact, Quote, QuotedProduct
from .utils import createProduct, createCompany, createQuote

# Create your views here.
def home(request):

    return render(request, "quote/quote_index.html")


def create_quote(request):

    if request.method == "GET":

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
        products = Product.objects.all()
        for product in products:
            product_options.append(
                {"id": product.id, "info": f"{product.pn}: {product.title}"}
            )

        return render(
            request,
            "quote/create-quote.html",
            {
                "company_options": company_options,
                "contact_options": contact_options,
                "product_options": product_options,
            },
        )
    elif request.method == "POST":

        data = request.POST

        # user = request.user
        user = User.objects.get(pk=1)

        print(user)

        company_id = data["company"].split(":")[0]

        contact_id = data["contact"].split(":")[0]
        print(contact_id)

        referente = data["reference"]

        date = data["date"]

        description = data["description"]

        terms = data["terms"]

        shipping = data["shipping"]

        tax = data["tax"]

        internal_notes = data["internal-notes"]

        quote = Quote(
            creator=user,
            reference=referente,
            short_description=description,
            company=Company.objects.get(pk=company_id),
            contact=Contact.objects.get(pk=contact_id),
            terms=terms,
            tax=tax,
            internal_note=internal_notes,
        )

        quote.save()
        print(quote.pk)

        # for i in range(data["product_options"]):
        #     product_pn = data["product_options"][i].split(":")[0]
        #     product_decription = data["custom-product-description"][i]
        #     qty = data["qty"][i]
        #     price = data["price"][i]
        #     discount = data["discount"][i]
        #     hidden = data["hidden"][i]

        return HttpResponseRedirect(reverse("create-quote"))


def request_product_options(request):

    product_options = Product.objects.all().values("pn")
    product_options = [d["pn"] for d in product_options]

    return JsonResponse({"product_options": product_options})


def get_product_info(request, pn):

    product = Product.objects.get(pn=pn)

    return JsonResponse(product.serialize(), safe=False)
