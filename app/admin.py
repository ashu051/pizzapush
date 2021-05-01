from django.contrib import admin
from .models import Customer,MyCart,Product,OrderPlaced,Rating
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','pincode','locality','nearLandmark']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','title','product_price','description','category','product_image']

@admin.register(MyCart)
class CartAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']
  
@admin.register(OrderPlaced)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordererd_date','status']
@admin.register(Rating)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','user','rate','rating']
