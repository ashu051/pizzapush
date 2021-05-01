from django.urls import path,include
from django.conf import settings
from app import views
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name="home"),
    path('cart/',views.cart,name="cart"),
    path('profile/',views.ProfileView.as_view(),name="profile"),
    path('product/',views.ProductData,name="product"),
    path('product/<slug:data>',views.ProductData,name="productdata"),
    path('product-detail/<int:pk>/',views.detail,name="detaildata"),
    path('addstar/<int:id1>/<int:p>',views.addstar,name="addstar"),
    path('addtocart/',views.addtocart,name="addtocart"),
    path('plus/',views.plus,name="plus"),
    path('minus/',views.minus,name="minus"),
    path('remove/',views.remove,name="remove"),
    path('order/',views.order,name="order"),
    path('paymentdone/',views.payment_done,name="paymentdone"),
    path('allorder/',views.allorder,name="orders")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
