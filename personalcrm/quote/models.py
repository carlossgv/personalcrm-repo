from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.deletion import PROTECT


class User(AbstractUser):
    pass


class Product(models.Model):
    pn = models.CharField(max_length=50, primary_key=True)
    description = models.TextField()
    list_price = models.IntegerField()
    multiplier = models.DecimalField(max_digits=5, decimal_places=3)
    creator = models.ForeignKey(User, on_delete=PROTECT, related_name="product_creator")
    editor = models.ForeignKey(User, on_delete=PROTECT, related_name="product_editor")
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)


class Company(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    mobile = models.CharField(max_length=12)
    category = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    creator = models.ForeignKey(User, on_delete=PROTECT, related_name="company_creator")
    editor = models.ForeignKey(User, on_delete=PROTECT, related_name="company_editor")
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    company = models.ForeignKey(
        Company, on_delete=PROTECT, related_name="company_contact"
    )
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    mobile = models.CharField(max_length=12)
    position = models.CharField(max_length=50)
    creator = models.ForeignKey(User, on_delete=PROTECT, related_name="contact_creator")
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)


class Quote(models.Model):
    creator = models.ForeignKey(
        User, on_delete=PROTECT, related_name="quote_creator", blank=False
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField("Product")
    company = models.ForeignKey(
        Company, on_delete=PROTECT, related_name="company_quoted"
    )
    contact = models.ForeignKey(
        Contact, on_delete=PROTECT, related_name="contact_quoted"
    )
