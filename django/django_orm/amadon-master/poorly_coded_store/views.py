from django.shortcuts import render
from .models import Order, Product

def index(request):
    request.session['total_money'] = 0
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)
# originally, there is only one checkout method that deals with render and post data, now two seperate methods are used according to solution
def purchase(request): # most of part, copy from solution, especially the if else structure
    def purchase(request):
        if request.method == 'POST':
            this_product = Product.objects.filter(id=request.POST["id"])
            if not this_product:
                return redirect('/')
            else:
                quantity_from_form = int(request.POST["quantity"])
                this_product = Product.objects.get(id=request.POST["product_id"])
                total_charge = quantity_from_form * this_product.price
                print("Charging credit card...")
                new_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
                return redirect('/checkout')
        else:
            return redirect('/')


def checkout(request):
    recent_order = Order.objects.last()
    this_payment = recent_order.total_price


    context = {
            # 'quantity_from_form': quantity_from_form,
            # 'price_from_form' : price_from_form,
            'this_payment': this_payment,
            'all_orders': Order.objects.all(),
            
        }

    return render(request, "store/checkout.html",context)