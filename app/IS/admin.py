from django.contrib import admin
from .models import Product
from django.contrib.auth.models import *
from .models import Product

import transformers
import tqdm
import torch
import numpy
import sklearn
import scipy
import nltk
import vncorenlp

import os,sys
sys.path.append("/home/loliology/Desktop/IS_app/app/IS/sentence_transformers")

import NeuralNet

# Register your models here.

admin.site.unregister(Group)
admin.site.unregister(auth.models.User)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['description_s']

    def change_view(self, request, object_id):
        source_user = request.POST.get('name', None)
        if source_user is not None:
            g = request.POST.copy()            
            request.POST = g
        return super(ProductAdmin, self).change_view(request, object_id)

    def changelist_view(self, request, extra_context=None):
        response = super(ProductAdmin, self).changelist_view(request, extra_context)
        filtered_query_set = response.context_data["cl"].queryset
        products = filtered_query_set.values('id')
        n = NeuralNet.NeuralNet()
        for pd in products:
            product = Product.objects.get(id=pd['id'])
            # print("pd review", product.review)
            if (product.review is not None):
                classify = n.encode(product.review)
                product.classify = classify
                product.save()
        return response
    
admin.site.register(Product, ProductAdmin)