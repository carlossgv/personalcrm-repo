from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.deletion import PROTECT


class User(AbstractUser):
    pass


class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


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


class Company(models.Model):
    name = models.CharField(max_length=20, unique=True)
    id_number = models.CharField(max_length=10, null=True, unique=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=12, null=True)
    mobile = models.CharField(max_length=12, null=True)
    category = models.ForeignKey(
        Category, on_delete=PROTECT, related_name="company_category"
    )
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=50, null=True)
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
        return f"{self.first_name} {self.last_name} | {self.company}"


class Quote(models.Model):
    creator = models.ForeignKey(User, on_delete=PROTECT, related_name="quote_creator")
    reference = models.CharField(max_length=50, blank=True, null=True)
    short_description = models.CharField(max_length=50, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField("Product", blank=True)
    company = models.ForeignKey(
        Company, on_delete=PROTECT, related_name="company_quoted"
    )
    contact = models.ForeignKey(
        Contact, on_delete=PROTECT, related_name="contact_quoted", blank=True, null=True
    )
    note = models.TextField(blank=True, null=True)


    def __str__(self) -> str:
        return (
            f"{self.pk} | {self.creator} | {self.reference} | {self.short_description}"
        )
