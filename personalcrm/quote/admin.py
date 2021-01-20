from django.contrib import admin
from .models import User, Product, Quote, Company, Contact

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Quote)
admin.site.register(Company)
admin.site.register(Contact)
