from django.shortcuts import render
from .models import User, Company

# Create your views here.
def home(request):

    return render(request, "quote/index.html")
