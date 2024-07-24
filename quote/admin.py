from django.contrib import admin

from .models import Company, Item, Quote

admin.site.register(Quote)
admin.site.register(Item)
admin.site.register(Company)
