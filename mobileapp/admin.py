from django.contrib import admin
from mobileapp.models import Brand,Product

# Register your models here.
admin.site.register(Brand)
admin.site.register(Product)

#create a superuser
#python3 manage.py createsuperuser
