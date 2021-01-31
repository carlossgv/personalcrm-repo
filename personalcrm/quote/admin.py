from django.contrib import admin
from .models import User, Category, Company, Contact, Product, Quote, QuotedProduct

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Quote)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(QuotedProduct)
