from django.urls import path
from . import views  
   
urlpatterns = [
    path('listings_protected/', views.ListingsProtected.as_view(), name ='listings'),
    path('listing_create/', views.ListingCreateProtected.as_view(), name='listing_create'),
]