from django.test import TestCase, Client, client
from django.urls import reverse
from rest_framework import status
import json
from rest.models import Users
from rest.serializers import RegistrationSerializer, LoginSerializer, ProductSerializer, SellerSerializer
# Create your tests here.


class GetAllTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        Users.objects.create(
            first_name='test', last_name='test_test', 
            email='test@test.com', password='123', repeat_password='123')
        
        Users.objects.get(email='test@test.com', password='123')
        

    def test_get_all_users_registration(self):
        response = self.client.get(reverse('registration_list'))
        user = Users.objects.all()
        serializer = RegistrationSerializer(user, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_all_users_login(self):
        response = self.client.get(reverse('login_list'))
        user = Users.objects.all()
        serializer = LoginSerializer(user, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_valid_single_user(self):
        response = self.client.get(
            reverse('login_detail', kwargs={'pk': '1'}))
        users = Users.objects.get(pk=1)
        serializer = LoginSerializer(users)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class CreateNewUserTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            'first_name': 'test',
            'last_name': 'test_test',
            'email': 'test@test.com',
            'password': '123',
            'repeat_password': '123'

        }
        self.invalid_payload = {
            'first_name': 'test1',
            'last_name': '',
            'email': '',
            'password': '123',
            'repeat_password': '123'
        }

    def test_create_valid_user(self):
        response = self.client.post(
            reverse('registration_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_invalid_user(self):
        response = self.client.post(
            reverse('registration_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
