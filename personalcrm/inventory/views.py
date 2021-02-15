from django.shortcuts import render

# ! INVENTORY VIEWS
def home(request):

    return render(request, "inventory/index.html")
