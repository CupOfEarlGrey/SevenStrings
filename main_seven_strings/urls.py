from django.urls import path
from . import views

app_name = 'main_seven_strings'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('shop/', views.shop_view, name='shop'),
    path('shop/search/', views.shop_search, name='shop_search'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
