
from django.urls import path,include
from .views import index,registration,login_view,logout_view,user_home,icon_detail,add_to_cart,view_mycart,remove_cartitem
urlpatterns=[
    path("",index,name="index"),
    path('account',registration,name="registration"),
    path('signin',login_view,name="signin"),
    path('signout',logout_view,name="signout"),
    path("home",user_home,name="home"),
    path("detail/<int:id>",icon_detail,name="itemdetail"),
    path('carts/<int:id>',add_to_cart,name="addtocart"),
    path('carts',view_mycart,name="viewmycart"),
    path('removecart/<int:id>',remove_cartitem,name="removecart")
]