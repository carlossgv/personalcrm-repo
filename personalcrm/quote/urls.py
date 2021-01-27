from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="quote-home"),
    path("create-quote", views.create_quote, name="create-quote"),
]
