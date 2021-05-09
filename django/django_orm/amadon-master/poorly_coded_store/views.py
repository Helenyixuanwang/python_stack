from django.shortcuts import render
from .models import Order, Product

def index(request):
    request.session['total_money'] = 0
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    
        
    print("Charging credit card...")
    new_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)



    context = {
            'quantity_from_form': quantity_from_form,
            'price_from_form' : price_from_form,
            'total_charge': total_charge,
            'all_orders': Order.objects.all(),
            
        }

    return render(request, "store/checkout.html",context)