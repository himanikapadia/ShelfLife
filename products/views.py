from django.shortcuts import get_object_or_404, render
from .models import Product

def product_list(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category:
        products = products.filter(category__iexact=category)

    categories = Product.objects.values_list(
        'category', flat=True
    ).distinct()

    return render(request, 'products/product_list.html', {
        'products': products,
        'query': query,
        'category': category,
        'categories': categories,
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'products/product_detail.html', {
        'product': product
    })