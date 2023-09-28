from django.urls import path,include
from . import views
from .views import chat, product_search, new_arrivals, product_details,create_product,create_category
from django.contrib.auth import views as auth_views
app_name = 'chatbot'
urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),
    path('chat/', views.chat, name='chat'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/create_category/', create_category, name='create_category'),
    path('api/create_product/', create_product, name='create_product'),
    path('product_search/', product_search, name='product_search'),
    path('new_arrivals/', new_arrivals, name='new_arrivals'),
    path('product/<int:product_id>/', product_details, name='product_details'),
    path('api/product/<str:product_name>/', views.product_details_api, name='product-details-api'),
    #path('recommendations/', views.recommendation_view, name='recommendations'),
    path('recommendations/', views.recommendation_view, name='recommendation_view'),
     path('customer_service/', views.customer_service_view, name='customer_service_view'),
     #path('size_and_fit_input/', views.size_and_fit_input_view, name='size_and_fit_input_view'),
     #path('kids_size_input/', views.get_kids_size_recommendations, name='kids_size_recommendations'),
    path('kids_size_recommendation/', views.kids_size_recommendation, name='kids_size_recommendation'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('display_recommendations/', views.display_recommendations, name='display_recommendations'),  # Include auth URLs
]
