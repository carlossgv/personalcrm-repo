from django.contrib import admin
from .models import User, Brand, Category, Company, Contact, Product, Quote, QuotedProduct, UserCompany

admin.site.register(User)
admin.site.register(Brand)
admin.site.register(UserCompany)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Quote)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(QuotedProduct)
