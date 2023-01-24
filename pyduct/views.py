from django.shortcuts import render
from pyduct.models import Product


def index(request):
    """
    pybo 목록출력
    """
    product_list = Product.objects.order_by('-create_date')
    context = {'product_list': product_list}
    return render(request, 'pyduct/product_list.html', context)

def detail(request, product_id):
    """
    pybo 내용출력
    """
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'pyduct/product_detail.html', context)