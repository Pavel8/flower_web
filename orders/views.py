from django.shortcuts import render

def order_list(request):
    return render(request, 'orders/order_list.html')

def order_detail(request, order_id):
    return render(request, 'orders/order_detail.html', {'order_id': order_id})

def create_order(request):
    return render(request, 'orders/create_order.html')
