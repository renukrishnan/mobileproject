from django.shortcuts import render,redirect
from customer.forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login as djangologin,logout
from mobileapp.models import Product,Cart
from mobileapp.views import get_object as get_product

# Create your views here.
#listed below are the things we need to do for customer.
#registration
#login
#logout
#viewproducts
#Add to cart.
#place orders
#manage orders
# django is allowing us to create app that means it is providing us all this registrations ,login, logout.
#that is called authentication app
# in django it is by using "auth" app means authentication.
# if we want to use auth then we have to register like application, in settings but it is already installed in settings.
#auth contains urls,models,views,forms
#the models in auth is called "user" model. there are many other models in auth . we are using user model

def index(request):
    return render(request,"customer/index.html")

def registration(request,*args,**kwargs):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"customer/login.html")
        else:
            context["form"]=form

    return  render(request,"customer/registration.html",context)

def login_view(request,*args,**kwargs):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")#form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                djangologin(request,user)
                return redirect("home")
            else:
                context["form"]=form


    return render(request,"customer/login.html",context)

def logout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

def user_home(request,*args,**kwargs):

        mobiles=Product.objects.all()
        context={
            "mobiles":mobiles
        }
        return render(request,"customer/home.html",context)
def icon_detail(request,*args,**kwargs):
    id=kwargs.get("id")
    mobile=Product.objects.get(id=id)
    context={"mobile":mobile}
    return render(request,"customer/productdetail.html",context)

def add_to_cart(request,*args,**kwargs):
    pid=kwargs.get("id")
    product=get_product(pid)
    cart=Cart(product=product,user=request.user)
    cart.save()
    return redirect("viewmycart")

def view_mycart(request,*args,**kwargs):
    cart_items=Cart.objects.filter(user=request.user,status="ordernotplaced")
    context={
        "cart_items":cart_items
    }
    return render(request,"customer/mycart.html",context)


def remove_cartitem(request,*args,**kwargs):
    id=kwargs.get("id")
    cart=Cart.objects.get(id=id)
    cart.delete()
    return redirect("home")