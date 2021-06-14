from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ProductCreateForm
from .models import Product

# Create your views here.

def home(request):
    return redirect(request,"index.html")

def create_product(request):
    form=ProductCreateForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ProductCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("fetchitems")
        else:
            context["form"]=form
            return render(request, "product_create.html", context)# else part is to print error m,sg from clean fun in the form

    return render(request,"product_create.html",context)


#view for listing all products
def list_products(request):
    mobiles=Product.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"product_list.html",context)

def get_object(id):
    return Product.objects.get(id=id)

def edit_item(request,*args,**kwargs):
    #kwargs={"id":1}
    #*args--> tuple format
    #**kwargs-->dict format

    id=kwargs.get("id") # or kwargs[id]
    product=get_object(id)# get_object if from above view--> to reduce same code to get id . Instead of this one -->#product=Product.objects.get(id=id)
    form=ProductCreateForm(instance=product)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ProductCreateForm(instance=product,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("fetchitems")
    return render(request,"edit_product.html",context)

def product_details(request,*args,**kwargs):
    id = kwargs.get("id")  # or kwargs[id]
    product = get_object(id) # instead of this-->product=Product.objects.get(id=id)
    context = {}
    context["product"] = product
    return render(request,"product_details.html",context)
def delete_product(request,*args,**kwargs):
    id=kwargs.get("id")
    product=get_object(id)
    product.delete()
    return redirect("fetchitems")