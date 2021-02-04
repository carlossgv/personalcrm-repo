from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.deletion import CASCADE, PROTECT


class User(AbstractUser):
    pass


class UserCompany(models.Model):
    user = models.ForeignKey(User, on_delete=PROTECT, related_name="user_company")
    name = models.CharField(max_length=50)
    legal_id = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"


class Product(models.Model):
    pn = models.CharField(max_length=50, unique=True)
    brand = models.ForeignKey(Brand, on_delete=PROTECT, related_name="brand_name")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    list_price = models.IntegerField(null=True)
    multiplier = models.DecimalField(
        max_digits=5, decimal_places=3, null=True, blank=True
    )
    creator = models.ForeignKey(User, on_delete=PROTECT, related_name="product_creator")
    editor = models.ForeignKey(User, on_delete=PROTECT, related_name="product_editor")
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.pn} | {self.title}"

    def serialize(self):
        return {
            "pn": self.pn,
            "brand": self.brand.name,
            "title": self.title,
            "description": self.description,
            "list_price": self.list_price,
            "multiplier": self.multiplier,
            "creator": self.creator.username,
            "editor": self.editor.username,
            "creation_date": self.creation_date,
            "edit_date": self.edit_date,
            "note": self.note,
        }


class Company(models.Model):
    name = models.CharField(max_length=20, unique=True)
    legal_id = models.CharField(max_length=10, null=True, unique=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=12, null=True)
    mobile = models.CharField(max_length=12, null=True)
    category = models.ForeignKey(
        Category, on_delete=PROTECT, related_name="company_category"
    )
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    creator = models.ForeignKey(User, on_delete=PROTECT, related_name="company_creator")
    editor = models.ForeignKey(User, on_delete=PROTECT, related_name="company_editor")
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self) -> str:

        return f"{self.name} | {self.category}"


class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    company = models.ForeignKey(
        Company, on_delete=PROTECT, related_name="company_contact"
    )
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=12, null=True)
    mobile = models.CharField(max_length=12, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=PROTECT, related_name="contact_creator")
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} | {self.company.name}"


class Quote(models.Model):
    creator = models.ForeignKey(User, on_delete=PROTECT, related_name="quote_creator")
    reference = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField("Product", blank=True)
    company = models.ForeignKey(
        Company, on_delete=PROTECT, related_name="company_quoted"
    )
    contact = models.ForeignKey(
        Contact, on_delete=PROTECT, related_name="contact_quoted", blank=True, null=True
    )
    terms = models.TextField(blank=True, null=True)
    tax = models.FloatField(blank=True, null=True)
    internal_note = models.TextField(blank=True, null=True)

    def serialize(self):
        return {
            "id": self.pk,
            "customer": self.company.name,
            "description": self.description,
            "reference": self.reference,
            "creator": self.creator.username,
        }

    def __str__(self) -> str:
        return (
            f"{self.pk} | {self.creator} | {self.reference} | {self.description}"
        )


class QuotedProduct(models.Model):
    quote = models.ForeignKey(Quote, on_delete=CASCADE, related_name="original_quote")
    product = models.ForeignKey(
        Product, on_delete=PROTECT, related_name="original_product"
    )
    description = models.TextField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    hidden = models.BooleanField(default=False)

    def serialize(self):
        return {
            "id": self.pk,
            "pn": self.product.pn,
            "title": self.product.title,
            "description": self.description,
            "qty": self.qty,
            "price": self.price,
            "discount": self.discount,
            "hidden": self.hidden,
        }

    def __str__(self) -> str:
        return f"{self.quote.pk} | {self.quote.creator} | {self.quote.description} | {self.product}"
