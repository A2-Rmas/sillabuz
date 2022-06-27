from django.shortcuts import render

from django.views.generic import (
    ListView as BaseListView,
    DetailView as BaseDetailView, 
)

from portafolios.blog.models import Blog

class ListView(BaseListView):
    model = Blog
    template_name = "storefront/blog/list.html"

class DetailView(BaseDetailView):
   model = Blog
   template_name = "storefront/blog/detail.html"
