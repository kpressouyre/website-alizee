from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.allProducts, name='index'),
    path('<int:product_id>/', views.oneProduct, name='product'),
]