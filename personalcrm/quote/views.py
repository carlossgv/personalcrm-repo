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
        products_list = Product.objects.all()
        for product in products_list:
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
        # TODO CHANGE USER TO CURRENT USER OR SELECT USER
        user = User.objects.get(pk=1)

        company_id = data["company"].split(":")[0]

        # TODO CATCH ERROR WHEN THERES NO USER ASSIGNED
        contact_id = data["contact"].split(":")[0]

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
            shipping=shipping,
            terms=terms,
            tax=tax,
            internal_note=internal_notes,
        )

        # create quote
        quote.save()

        quote = Quote.objects.all().order_by("-id")[0]
        # print(quote)

        # lists of each item's row
        products_list = request.POST.getlist("product-options")
        products_description_list = request.POST.getlist("custom-product-description")
        qty_list = request.POST.getlist("qty")
        price_list = request.POST.getlist("price")
        discount_list = request.POST.getlist("discount")
        hidden_list = request.POST.getlist("hidden")

        # add products to quote
        for i in range(len(products_list)):
            product_pn = products_list[i].split(":")[0]
            product_object = Product.objects.get(pn=product_pn)

            # add products to quote
            quote.products.add(product_object)

            # convert hidden values
            if hidden_list[i] == 'True':
                hidden_list[i] = True
            else:
                hidden_list[i] = False

            # add products particular info to quotedproducts
            quoted_info = QuotedProduct(
                quote = quote,
                product = product_object,
                description = products_description_list[i],
                qty = qty_list[i],
                price = price_list[i],
                discount = discount_list[i],
                hidden = hidden_list[i],
            )

            quoted_info.save()

        return HttpResponseRedirect(reverse("create-quote"))


def request_product_options(request):

    product_options = Product.objects.all().values("pn")
    product_options = [d["pn"] for d in product_options]

    return JsonResponse({"product_options": product_options})


def get_product_info(request, pn):

    product = Product.objects.get(pn=pn)

    return JsonResponse(product.serialize(), safe=False)
