from .models import Customer,Product,MyCart,OrderPlaced,Rating
from django.contrib.auth.models import User
from drf_writable_nested.serializers import WritableNestedModelSerializer

from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields=['id','user','name','pincode','locality','state','nearLandmark','customerorder',]

class ProductSerializer(serializers.ModelSerializer):
    cpnigga=serializers.StringRelatedField(many=True)
    clasr3=serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields=['id','title','description','product_price','category','product_image','cpnigga','clasr3']

class MyCartSerializer(serializers.ModelSerializer):
    # user=UserSerializer(read_only=False)
    class Meta:
        model = MyCart
        fields=['id','quantity','product','user',]

class OrderPlacedSerializer(serializers.ModelSerializer):
    # userorder =serializers.StringRelatedField(many=True)
    # customerorder =serializers.StringRelatedField(many=True)
    # productorder =serializers.StringRelatedField(many=True)
    all_data = serializers.ReadOnlyField()
    class Meta:
        model = OrderPlaced
        fields=['id','quantity','ordererd_date','status','user','customer','product','all_data']
    

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields=('id','rating','user','rate')
class UserSerializer(WritableNestedModelSerializer):
    order_set  = OrderPlacedSerializer(many=True,read_only=True)
    print(order_set)
    cart_set  = MyCartSerializer(many=True,read_only=True)
    rating_set = RatingSerializer(many=True,read_only=True)
    cus_set = CustomerSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields=['id','username','password','order_set','cart_set','cus_set','rating_set']
    
