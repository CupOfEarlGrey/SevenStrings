from django.db.models import Q
from django.shortcuts import render
from .models import *
from cart.cart import Cart
from itertools import chain


# Create your views here.


def main_page(request, category_slug=None):
    cart = Cart(request)
    e_guitars = Product.objects.filter(category="Electric Guitar").filter(available=True).filter(featured=True)
    a_guitars = Product.objects.filter(category="Acoustic Guitar").filter(available=True).filter(featured=True)
    accessories = Product.objects.filter(category="Accessories").filter(available=True).filter(featured=True)
    products = chain(e_guitars, a_guitars, accessories)
    return render(request, 'index.html',
                  {'e_guitars': e_guitars, 'a_guitars': a_guitars, "accessories": accessories,
                   'products': products, 'cart': cart})


def product_detail(request, id, slug):
    cart = Cart(request)
    products = Product.objects.filter(id=id).filter(slug=slug).filter(available=True)
    featured = Product.objects.filter(available=True).filter(featured=True)
    return render(request,
                  'product_page.html',
                  {'products': products, "featured": featured, 'cart': cart}
                  )


def get_brand_set():
    brand_set = []
    for i in Product.objects.values("brand"):
        if i not in brand_set:
            brand_set.append(i)
    return brand_set


def shop_view(request):
    cart = Cart(request)

    category = [item[0] for item in ProductCategory]
    brand = get_brand_set()
    featured = Product.objects.filter(featured=True)
    products = Product.objects.all()
    search_result = []

    if 'search_request' in request.GET:
        search_result = Product.objects.filter(available=True).filter(name__contains=request.GET.get("search_request"))
    if 'category' in request.GET:
        products = products.filter(category__in=request.GET.getlist("category"))
    if 'brand' in request.GET:
        products = products.filter(brand__in=request.GET.getlist("brand"))
    if 'first_price' in request.GET:
        products = products.filter(Q(price__gte=request.GET.get("first_price")), Q(price__lte=request.GET.get("last_price")))
    else:
        products = Product.objects.filter(available=True)

    return render(request, 'shop.html', {
        "products": products,
        "category": category,
        "brand": brand,
        "featured": featured,
        'cart': cart,
        "search_result": search_result,
    })


def shop_search(request):
    cart = Cart(request)

    search_result = Product.objects.filter(available=True).filter(name__contains=request.GET.get("search_request"))
    return render(request, "shop.html", {"search_result": search_result})
