from django.shortcuts import get_object_or_404
from rest_framework import views, status
from rest_framework.response import Response
from .models import Buyer, Seller, Transaction
from .serializer import BuyerSerializer, \
        SellerSerializer, TransactionSerializer


# Create your views here.
# ----------------------Buyer API requests------------------------#
class BuyerList(views.APIView):
    def get(self, request, format=None):
        # gets a list of all the buyers
        buyers = Buyer.objects.all()
        serializer = BuyerSerializer(buyers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # creates a new buyer record
        serializer = BuyerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuyerDetail(views.APIView):
    def get(self, request, pk, format=None):
        # gets the details of a buyer using the primary key
        buyer = get_object_or_404(Buyer.objects.all(), pk=pk)
        serializer = BuyerSerializer(buyer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        # updates a buyer's details
        buyer = get_object_or_404(Buyer.objects.all(), pk=pk)
        serializer = BuyerSerializer(buyer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        # updates a buyer's details
        buyer = get_object_or_404(Buyer.objects.all(), pk=pk)
        serializer = BuyerSerializer(buyer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # deletes a buyer record
        buyer = get_object_or_404(Buyer.objects.all(), pk=pk)
        buyer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------------Seller API requests------------------------#
class SellerList(views.APIView):
    def get(self, request, format=None):
        # gets a list of all the sellers
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # creates a new seller record
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellerDetail(views.APIView):
    def get(self, request, pk, format=None):
        # gets the details of a seller using the primary key
        seller = get_object_or_404(Seller.objects.all(), pk=pk)
        serializer = SellerSerializer(seller)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        # updates a seller's detail
        seller = get_object_or_404(Seller.objects.all(), pk=pk)
        serializer = SellerSerializer(seller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    def patch(self, request, pk, format=None):
        # updates a seller's detail
        seller = get_object_or_404(Seller.objects.all(), pk=pk)
        serializer = SellerSerializer(seller, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # deletes a seller record
        seller = get_object_or_404(Seller.objects.all(), pk=pk)
        seller.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# ----------------------Transaction API requests------------------------#
class TransactionList(views.APIView):
    def get(self, request, format=None):
        # gets a list of all the transactions
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # creates a new transaction
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionDetail(views.APIView):
    def get(self, request, pk, format=None):
        # gets the details of a transaction using the primary key
        transaction = get_object_or_404(Transaction.objects.all(), pk=pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)