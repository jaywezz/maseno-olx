from django.urls import include
from django .urls import path
from . import views
from django.urls import include



app_name = 'item_view'

urlpatterns = [

    path('', views.welcome_page, name='welcome_page'),
	 path('upload-item', views.UploadView.as_view(), name='upload-item'),
	 path('item_detail/<name>', views.item_detail, name='item_detail'),
	 path('cart', views.cart_detail, name='cart_detail'),
	 path('cart_detail', views.cart_detail, name='cart_detail'),
    path('add/<int:item_id>/',views.cart_add,name='cart_add'),
	 path('cart_remove', views.cart_remove, name='cart_remove'),


]