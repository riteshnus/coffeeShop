from django.shortcuts import render
from .models import Drink

# Create your views here.
def index(request):
    drinks = Drink.objects.all()
    return render(request, 'index.html', {'drinks': drinks})

def checkout(request):
    return render(request, 'checkout.html')

# class Drink:
#     def __init__(self, name, type, price):
#         self.name = name
#         self.type = type
#         self.price = price
#
# drinks = [
#     Drink('Espresso', 'coffee', dict(tall=[1.95, 'www'], grande=2.05, Venti=2.35)),
#     Drink('Latte', 'coffee', dict(tall=3.4, grande=4.45, Venti=4.65)),
#     Drink('Cappuccino', 'coffee', dict(tall=3.15, grande=3.75, Venti=4.155)),
#     Drink('Green Tea', 'tea', dict(tall=3.45, grande=4.25, Venti=4.45)),
#     Drink('Hot tea', 'tea', dict(grande=1.95))
# ]