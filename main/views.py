# views.py
from django.shortcuts import render
from goods.models import Categories, Products
from django.shortcuts import get_object_or_404, render


def buypage(request, category_slug=None):
    categories = Categories.objects.all()
    products = Products.objects.all()

    if category_slug:
        products = products.filter(category__slug=category_slug)

    context = {
        "categories": categories,
        "goods": products,
        "category_slug": category_slug,
    }
    return render(request, "main/buypage.html", context)



def about(request):
    context = {
        'title': 'О нас',
        'content': "О нас",
        'textonpage': "СЛОВО СЛОВО СЛОВО",
    }


    return render(request, 'main/about.html', context)

def product(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)
    context = {
        'product': product
    }

    return render(request, "goods/product.html", context=context)


