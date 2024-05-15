from django.shortcuts import get_object_or_404, render
from goods.models import Products

def catalog(request, category_slug=None):
    if category_slug == 'all' or category_slug is None:
        goods = Products.objects.all()
    elif category_slug == 'kolechki':
        goods = Products.objects.filter(category__slug=category_slug)
    elif category_slug == 'seryozhki':
        goods = Products.objects.filter(category__slug=category_slug)
    elif category_slug == 'drugoe':
        goods = Products.objects.filter(category__slug=category_slug)
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    context = {
        "title": "Украшения Мари - Каталог",
        "goods": goods, 
        "category_slug": category_slug,  # Добавляем текущую категорию в контекст

    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)

    context = {
        'product': product
    }

    return render(request, "goods/product.html", context=context)
