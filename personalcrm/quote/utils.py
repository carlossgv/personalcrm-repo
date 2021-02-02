from .models import User, Product, Company, Contact, Quote, QuotedProduct


def create_or_edit_quote(data, user, method, quote_id=""):
    # general info
    company_id = data["company"].split(":")[0]
    # TODO CATCH ERROR WHEN THERES NO USER ASSIGNED
    contact_id = data["contact"].split(":")[0]
    reference = data["reference"]
    date = data["date"]
    description = data["description"]
    terms = data["terms"]
    shipping = data["shipping"]
    tax = data["tax"]
    internal_notes = data["internal-notes"]

    # products info
    products_list = data.getlist("product-options")
    products_description_list = data.getlist("custom-product-description")
    qty_list = data.getlist("qty")
    price_list = data.getlist("price")
    discount_list = data.getlist("discount")
    hidden_list = data.getlist("hidden")

    if method == "create":

        quote = Quote(
            creator=user,
            reference=reference,
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

    elif method == "edit":
        quote = Quote.objects.filter(pk=quote_id)

        quote.update(
            creator=user,
            reference=reference,
            short_description=description,
            company=Company.objects.get(pk=company_id),
            contact=Contact.objects.get(pk=contact_id),
            shipping=shipping,
            terms=terms,
            tax=tax,
            internal_note=internal_notes,
        )

        quote = quote[0]
        # remove products from quote to add them below
        for i in range(len(products_list)):
            product_pn = products_list[i].split(":")[0]
            product_object = Product.objects.get(pn=product_pn)
            quote.products.remove(product_object)

        # delete all items from quotedproduct and add them again below
        QuotedProduct.objects.filter(quote=quote).delete()

    # add products to quote
    for i in range(len(products_list)):
        product_pn = products_list[i].split(":")[0]
        product_object = Product.objects.get(pn=product_pn)

        # add products to quote
        quote.products.add(product_object)

        # convert hidden values
        if hidden_list[i] == "True":
            hidden_list[i] = True
        else:
            hidden_list[i] = False

        # add products particular info to quotedproducts
        quoted_info = QuotedProduct(
            quote=quote,
            product=product_object,
            description=products_description_list[i],
            qty=qty_list[i],
            price=price_list[i],
            discount=discount_list[i],
            hidden=hidden_list[i],
        )

        quoted_info.save()

    if method == "create":
        return "quote created"
    elif method == "edit":
        return f"quote {quote_id} edited"


def createProduct(pn, creator, editor, description="", list_price="", multiplier=""):

    product = Product(
        pn=pn,
        description=description,
        list_price=list_price,
        multiplier=multiplier,
        creator=creator,
        editor=editor,
    )
    return product


def createCompany(
    name,
    creator,
    editor,
    email="",
    phone="",
    mobile="",
    category="",
    address="",
    city="",
    country="",
):

    company = Company(
        name=name,
        creator=creator,
        editor=editor,
        email=email,
        phone=phone,
        mobile=mobile,
        category=category,
        address=address,
        city=city,
        country=country,
    )
    return company
