from django.urls import path, include
from rest import views
# from rest_framework import routers


from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('registration/', views.RegistrationList.as_view()),
    path('registration/<int:pk>/', views.RegistrationDetail.as_view()),
    
    path('login/', views.LoginList.as_view()),
    path('login/<int:pk>/', views.LoginDetail.as_view()),
    
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    
    path('seller/', views.SellerList.as_view()),
    path('seller/<int:pk>/', views.SellerDetail.as_view()),

    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
