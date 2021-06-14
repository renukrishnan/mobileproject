from django.forms import ModelForm
from .models import Product
from django import forms

class ProductCreateForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__" # to get all fields from that model, product
        widgets={
            "mobile_name":forms.TextInput(attrs={"class":"form-control p-2"}),
            "price":forms.TextInput(attrs={"class":"form-control p-2"}),
            "specs":forms.Textarea(attrs={"class":"form-control p-2"})

        }# widgets is to style form

    def clean(self):# clean method is to validate form
        cleaned_data=super().clean()
        price=self.cleaned_data.get("price")
        if price<500:
            msg="Invalid price"
            self.add_error("price",msg)