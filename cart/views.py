from django.shortcuts import render

def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

def cart_add(request, product_id):
    return render(request, 'cart/cart_add.html', {'product_id': product_id})

def cart_remove(request, product_id):
    return render(request, 'cart/cart_remove.html', {'product_id': product_id})
