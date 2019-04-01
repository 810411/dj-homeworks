from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Phone


def index(request):
    return redirect(reverse(show_catalog))


def show_catalog(request):
    sort = request.GET.get('sort')

    if sort:
        phones = Phone.objects.order_by(sort)
    else:
        phones = Phone.objects.all()

    context = {
        'phones': phones
    }

    return render(
        request,
        'catalog.html',
        context
    )


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)

    context = {
        'phone': phone
    }

    return render(
        request,
        'product.html',
        context
    )
