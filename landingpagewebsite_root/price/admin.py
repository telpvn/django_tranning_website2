from django.contrib import admin
from .models import PriceCart, PriceTable

# Register your models here.
admin.site.register(PriceTable)
admin.site.register(PriceCart)
