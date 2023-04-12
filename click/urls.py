from django.urls import path
from . import views  
   
urlpatterns = [
    path('click/', views.ListingsProtected.as_view(), name ='listings'),
    path('click_create/', views.ListingCreateProtected.as_view(), name='listing_create'),
    path('click_edit/<uuid:pk>/', views.ListingDetailProtected.as_view(), name='listing_edit'),
]