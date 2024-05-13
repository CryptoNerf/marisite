from django.shortcuts import render
from django.template import context


def catalog(request):
    context = {
        "title": "Украшения Мари - Каталог",
        "goods": [
            {
                "image": "deps/image/грибочкисерьга.png",
                "name": "pagegood1"
            },
            {
                "image": "deps/image/грибочкисерьга.png",
                "name": "Чайный столик и два стула"
            },
            {
                "image": "deps/image/грибочкисерьга.png",
                "name": "Двухспальная кровать"
            },
            {
                "image": "deps/image/грибочкисерьга.png",
                "name": "Кухонный стол с раковиной"
            },
            {
                "image": "deps/image/грибочкисерьга.png",
                "name": "Кухонный стол с встройкой"
            },
            {
                "image": "deps/image/грибочкисерьга.png",
                "name": "Угловой диван для гостинной"
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
