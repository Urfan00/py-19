from django.shortcuts import render
from product.models import Product




def product_list(requests):

    product_objects = Product.objects.all() 

    context = {
        'products' : product_objects
    }


    return render(requests, 'product_list.html', context)
