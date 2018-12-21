from django.shortcuts import render
from . models import Categories, SubCategories, Products
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
UpdateView)
from django.shortcuts import render

# Create your views here.

def home(request):
    response = []
    query = Products.objects.all()

    for i in query:
        dic = {}
        dic['product'] = str(i)
        dic['sub_category'] = str(i.sub_category)
        dic['category'] = str(i.sub_category.category)
        response.append(dic)

    return  render(request,'index.html', {'stuff': response})











