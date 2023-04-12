from django.urls import path
from . import views  
   
urlpatterns = [
    path('click/', views.ClickRead.as_view(), name ='clicks'),
    path('click_create/', views.ClickCreate.as_view(), name='click_create'),
    path('click_edit/<uuid:pk>/', views.ClickDetail.as_view(), name='click_edit'),
]