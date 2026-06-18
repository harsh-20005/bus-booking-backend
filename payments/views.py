from django.shortcuts import render

# Create your views here.
import razorpay
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
# Initializes the Razorpay client with the API key ID and secret from the Django settings.
# This client will be used to make API calls to Razorpay.


# This view is decorated with @api_view(['POST']), indicating that it only accepts POST requests.
# The function create_order handles the creation of a payment order.
@api_view(['POST'])
def create_order(request):
    amount = request.data.get('amount')  # amount in rupees
    amount_paise = int(float(amount) * 100)  # convert to paise

    payment = client.order.create({
        "amount": amount_paise,
        "currency": "INR",
        "payment_capture": 1
    })
# Calls the Razorpay API to create a new order with the specified amount, currency, and payment capture option.
# The payment_capture set to 1 means that the payment will be captured automatically upon successful authorization.


    return Response({
        "order_id": payment['id'],
        "amount": payment['amount'],
        "currency": payment['currency'],
        "key_id": settings.RAZORPAY_KEY_ID
    })


# Returns a JSON response containing:
# order_id: The unique ID of the created order.
# amount: The amount for the order in paise.
# currency: The currency type (INR).
# key_id: The Razorpay key ID, which can be used on the client side for further payment processing.