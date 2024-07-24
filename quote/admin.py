from django.contrib import admin

from .models import Quote, Item, Company

admin.site.register(Quote)
admin.site.register(Item)
admin.site.register(Company)