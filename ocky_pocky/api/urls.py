from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('categories', views.categories),
    path('sub-categories', views.sub_categories),
    path('product', views.ProductList.as_view())
]

