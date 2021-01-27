from .models import User, Product, Company, Quote


def createQuote(
    company, creator, products="", contact="", reference="", short_description=""
):

    quote = Quote(
        company=company,
        creator=creator,
        contact=contact,
        reference=reference,
        short_description=short_description,
    )

    quote.save()

    for product in products:
        quote.products.add(product)

    return "quote created"


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
