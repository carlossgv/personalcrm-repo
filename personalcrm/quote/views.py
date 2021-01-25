from django.shortcuts import render
from .models import User, Company
from .utils import createProduct, createCompany

# Create your views here.
def home(request):

    companies = Company.objects.get(pk=5)
    print(companies)

    return render(request, "quote/index.html")
