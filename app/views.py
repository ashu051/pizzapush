from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import CustomerProfileForm
from django.views import View
from .models import Customer,Product,MyCart,OrderPlaced,Rating
from django.http import JsonResponse
from django.db.models import Q
import math
from rest_framework import viewsets

from django.contrib import messages
from django.contrib.auth.models import User
from .serializers import UserSerializer,OrderPlacedSerializer, MyCartSerializer,ProductSerializer,CustomerSerializer,RatingSerializer
########################################         serializers section    start ################################################
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    print(queryset)
    serializer_class = UserSerializer
    print(serializer_class)
 
class CustomerModelViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    print(queryset)
    serializer_class = CustomerSerializer
class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    print(queryset)
    serializer_class = ProductSerializer
class MyCartModelViewSet(viewsets.ModelViewSet):
    queryset = MyCart.objects.all()
    print(queryset)
    serializer_class = MyCartSerializer
class OrderPlacedModelViewSet(viewsets.ModelViewSet):
    queryset = OrderPlaced.objects.all()
    print(queryset)
    serializer_class = OrderPlacedSerializer
class RatingModelViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    print(queryset)
    serializer_class = RatingSerializer
########################################         serializers section    end ################################################

def index(request):
    return render(request,"app/index.html")

def cart(request):
    data1 = MyCart.objects.all()
    # data2 = list(set(data1))
    data2  = MyCart.objects.all()
    print(data1)
    print(data2)
    # mylis = []
    # c=0
    # for i in data2:
    #     mylis.append(i['product'])
    # print(mylis)
    price=0
    pro= MyCart.objects.all()
    for i in pro:
        price += i.product.product_price*i.quantity
    return render(request,"app/cart.html" , {'obj':data2,'price':price})

def addtocart(request):
    user=request.user
    product=request.GET.get('prod_id')
    print('------------------id------------------------------------------------------------')
    print(product)
    product_id=Product.objects.get(id=product)
    item_in_cart = MyCart.objects.filter(user=user,product=product_id)
    if len(item_in_cart) == 0:
        MyCart(user=user,product=product_id).save()
    else:
        messages.add_message(request, messages.WARNING, "already in cart")
        url="/product-detail/{}".format(product)
        return HttpResponseRedirect(url)

    return HttpResponseRedirect('/cart')






class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, "app/profile.html",{'form':form})
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Registered Successfullllyyyyy')
            form.save()
        return render(request,"app/profile.html",{'form':form})

def ProductData(request,data=None):
    if data == 'Pan':
        data1 = Product.objects.filter(category="pan")
        flag=1
    elif data == 'Burst':
        data1 = Product.objects.filter(category="burst")
        flag=2
    elif data == 'Hot':
        data1 = Product.objects.filter(category="hot")
        flag=3
    elif data == 'Corn':
        data1 = Product.objects.filter(category="Corn")
        flag=4
    elif data == 'Onion':
        data1 = Product.objects.filter(category="onion")
        flag=5
    elif data == 'Paneer':
        data1  = Product.objects.filter(category="paneer")
        flag=6
    elif data == None:
        data1 = Product.objects.all()
        flag=7

    return render(request,"app/product.html",{'data1':data1,'active':'btn btn-info','flag':flag})

def detail(request,pk):
    myp = Product.objects.get(id=pk)
    print('------------------myp-----------------------------------------------')
    print(myp)
    print(request.user)
    rating = Rating.objects.get_or_create(rate=myp,user=request.user)
    allobj = Rating.objects.filter(rate=myp)
    sum1=0
    for i in allobj:
        sum1+=i.rating
    print("sum is {sum1}")
    print(sum1)
    print("sum1")
    o = len(allobj)
    p = o*5
    value = (sum1/p)*100
    value = math.floor(value)
    print(o)
    return render(request, "app/product-detail.html",{'myp':myp,'c':rating[0].rating,'o':o,'sum':sum1,'p':p,'value':value})


def addstar(request,id1,p):
    if request.method== "GET":
        pro = Product.objects.get(id=id1)
        prod_id= request.GET.get('p')
        c = Rating.objects.filter(rate=pro,user=request.user)
        if len(c) == 0:
            Rating(rate=pro,user=request.user,rating=p).save()
        if len(c) == 1:
            g = Rating.objects.get(user=request.user,rate=pro)
            g.rating = p
            g.save()
        print('--------------------------------------------Value--------------------------------------------------')
        print(type(c))
        print(id1)
        print(p)
        url="/product-detail/{}".format(id1)
    return redirect(url)


def plus(request):
    productid = request.GET['product_id']
    print(productid)
    product=Product.objects.get(id=productid)
    cart = MyCart.objects.get(user=request.user,product=product)
    cart.quantity += 1
    cart.save() 
    price=0
    pro= MyCart.objects.all()
    lis = []
    print("nothing")
    for i in pro:
        if i.user == request.user:
            price += i.product.product_price*i.quantity
            print(i.quantity)
            print(i.product.product_price)
            print(i.product.id)
            print(price)
    print("we get price")            

    data={
            'quantity':cart.quantity,
            'price':price
        }
    return JsonResponse(data)

def minus(request):
    productid = request.GET['product_id']
    print(productid)
    product=Product.objects.get(id=productid)
    cart = MyCart.objects.get(user=request.user,product=product)
   
    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()
        price=0
        pro= MyCart.objects.all()
        for i in pro:
            if i.user == request.user:
                price += i.product.product_price*i.quantity
                print(i.quantity)
                print(i.product.product_price)
                print(i.product.id)
                print(price)
        data={
            'quantity':cart.quantity,
            'price':price
        }
        return JsonResponse(data)
    elif cart.quantity == 1:
        cart.quantity=1
        cart.save()
        price=0
        pro= MyCart.objects.all()
        for i in pro:
            if i.user == request.user:
                price += i.product.product_price*i.quantity
                print(i.quantity)
                print(i.product.product_price)
                print(i.product.id)
                print(price)
        data={
            'quantity':cart.quantity,
            'message': "Not less than One Item Quantity is one now",
            'price':price
        }
  
    return JsonResponse(data)
def remove(request):
    productid = request.GET['product_id']
    print(productid)
    product=Product.objects.get(id=productid)
    cart = MyCart.objects.get(user=request.user,product=product)
    cart.delete()
    pro= MyCart.objects.all()
    price=0
    for i in pro:
        if i.user == request.user:
            price += i.product.product_price*i.quantity
            print(i.quantity)
            print(i.product.product_price)
            print(i.product.id)
            print(price)

    data={
            'quantity':"Remove",
            'price':price
        }
    return JsonResponse(data)

# def order(request):
#     customer=Customer.objects.all()

#     return render(request, "app/order.html",{'customer':customer})

def order(request):
    user=request.user
    add = Customer.objects.filter(user=user)
    pro= MyCart.objects.filter(user=user)
    price=0.0
    for i in pro:
        price += i.product.product_price*i.quantity
    return render(request, 'app/order.html',{'add':add,'cart_items':pro,'total':price})

def payment_done(request):
    custid=request.GET.get('custid')
    user=request.user
    customer = Customer.objects.get(id=custid)
    cart=MyCart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect("orders")


def allorder(request):
    op=OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html',{'op':op})