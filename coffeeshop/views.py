from django.shortcuts import render
from .models import Drink
from rest_framework import status
from .models import Order
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import OrderSerializer


# Create your views here.
def index(request):
    drinks = Drink.objects.all()
    return render(request, 'index.html', {'drinks': drinks})


@api_view(['GET', 'POST'])
def OrderView(request):

    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        print(dict(request.data))
        requestOrdersArray = request.data['orders']
        responseData = []
        lastOrderId = 0
        serializerForGet = OrderSerializer(Order.objects.all(), many=True)
        if(len(serializerForGet.data) > 0):
            lastOrderId = serializerForGet.data[-1]['orderId']
        for order in requestOrdersArray:
            serializer = OrderSerializer(data=order)
            if serializer.is_valid():
                serializer.save(orderId=lastOrderId+1)
                responseData.append(serializer.data)
        return Response(responseData, status=status.HTTP_201_CREATED)
