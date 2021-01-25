from .models import User, Company


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
