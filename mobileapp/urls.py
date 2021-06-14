
from django.urls import path
from .views import home,create_product,list_products,edit_item,product_details,delete_product

urlpatterns = [
    path('',home,name="hm"),
    path('products',create_product,name="create_product"),
    path('items',list_products,name="fetchitems"),
    path('item/change/<int:id>',edit_item,name="change"),
    path('item/<int:id>',product_details,name="product_detail"),
    path('item/remove/<int:id>',delete_product,name="remove")
]