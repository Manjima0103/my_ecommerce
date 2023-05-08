from django.shortcuts import render

from django.shortcuts import render
from choco.models import Product, Category
from django.db.models import Q


def SearchResult(request):
    products = None
    query = None
    categories = []
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query))
        categories = Category.objects.filter(name__icontains=query)
    return render(request, 'search.html', {'query': query, 'products': products, 'categories': categories})
