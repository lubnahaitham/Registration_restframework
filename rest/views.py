from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest.models import Users, Products, Seller
from rest.serializers import RegistrationSerializer, LoginSerializer, ProductSerializer, SellerSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class RegistrationList(APIView):
    
    #this serializer model viewset to view it in restframework, remove the comment to use it
    
    # serializer_class = RegistrationSerializer
    
    """
    List all, or create a new.
    """

    def get(self, request, format=None):
        user_registration = Users.objects.all()
        serializer = RegistrationSerializer(user_registration, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RegistrationDetail(APIView):
    
    #this serializer model viewset to view it in restframework, remove the comment to use it
    
    # serializer_class = RegistrationSerializer

    """
    Retrieve, update or delete an instance.
    """
    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_registration = self.get_object(pk)
        serializer = RegistrationSerializer(user_registration)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_registration = self.get_object(pk)
        serializer = RegistrationSerializer(user_registration, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_registration = self.get_object(pk)
        user_registration.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginList(APIView):
    
    #this serializer model viewset to view it in restframework, remove the comment to use it
    
    # serializer_class = LoginSerializer
    
    """
    List all, or create a new.
    """

    def get(self, request, format=None):
        user_login = Users.objects.all()
        serializer = LoginSerializer(user_login, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginDetail(APIView):
    
    #this serializer model viewset to view it in restframework, remove the comment to use it
    
    # serializer_class = LoginSerializer

    """
    Retrieve, update or delete an instance.
    """
    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_login = self.get_object(pk)
        serializer = LoginSerializer(user_login)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_login = self.get_object(pk)
        serializer = LoginSerializer(user_login, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_login = self.get_object(pk)
        user_login.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductList(APIView):
    
    #this serializer model viewset to view it in restframework, remove the comment to use it
    
    # serializer_class = ProductSerializer
    
    """
    List all, or create a new.
    """

    def get(self, request, format=None):
        product = Products.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetail(APIView):
    
    #this serializer model viewset to view it in restframework, remove the comment to use it
    
    # serializer_class = ProductSerializer

    """
    Retrieve, update or delete an instance.
    """
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SellerList(APIView):
    
    #this serializer model viewset to view it in restframework, remove the comment to use it
    
    # serializer_class = SellerSerializer
    
    """
    List all, or create a new.
    """

    def get(self, request, format=None):
        seller = Seller.objects.all()
        serializer = SellerSerializer(seller, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SellerDetail(APIView):
    
    #this serializer model viewset to view it in restframework, remove the comment to use it
    
    # serializer_class = SellerSerializer

    """
    Retrieve, update or delete an instance.
    """
    def get_object(self, pk):
        try:
            return Seller.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        seller = self.get_object(pk)
        serializer = SellerSerializer(seller)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        seller = self.get_object(pk)
        serializer = SellerSerializer(seller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        seller = self.get_object(pk)
        seller.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
