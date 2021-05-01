
from django.contrib import admin
from django.urls import path,include
from app import views
from rest_framework.routers import DefaultRouter
from django.conf import settings

router = DefaultRouter()
router.register('products', views.ProductModelViewSet,basename="products"),
router.register('cart', views.MyCartModelViewSet,basename="cart"),
router.register('placeorder', views.OrderPlacedModelViewSet,basename="placeorder"),
router.register('rating', views.RatingModelViewSet,basename="rating"),
router.register('customer', views.CustomerModelViewSet,basename="customer"),
router.register('user', views.UserModelViewSet,basename="user"),
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
        path('', include('app.urls')),
        #  path('get/',include(router.urls)),

]
