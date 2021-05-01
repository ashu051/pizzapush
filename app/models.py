from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
state_choice = (
    ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)
class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='cus_set')
    name=models.CharField(max_length=20)
    pincode = models.CharField(max_length=10)
    state =  models.CharField(choices=state_choice,max_length=40)
    locality = models.CharField(max_length=30)
    nearLandmark = models.CharField(max_length=20)
    def __str__(self):
        return str(self.id)
category_choice = (
        ('pan','Pan Pizza'),
        ('burst','Burst Pizza'),
        ('hot','Chilli Mix'),
        ('Corn','Basic Corn'),
        ('onion','Fry Onion'),
        ('paneer','High Paneer'),
)

class Product(models.Model):
    title=models.CharField(max_length=20)
    product_image=models.ImageField(upload_to='productimages')
    product_price = models.FloatField()
    description=models.TextField()
    category = models.CharField(choices=category_choice,max_length=20)
    def __str__(self):
        return str(self.id)
    

    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='rating_set')
    rate= models.ForeignKey(Product, on_delete=models.CASCADE,related_name='clasr3')
    rating  = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)] ,default=1)
    def __str__(self):
        return str(self.id)
    

    

    

class MyCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='cart_set') 
    product  = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='cpnigga')
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity*self.product.product_price

status_choice=(
    ('Accepted','Accepted'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Packed','Packed'),
    ('Cancel','Cancel'),
    ('Pending','Pending')
)
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='order_set')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='customerorder')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='productorder')
    quantity = models.PositiveIntegerField(default=1)
    ordererd_date  = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=status_choice,default='Pending')
    @property
    def all_data(self):
        data = str(self.status) +  "  " + str(self.ordererd_date) +  "  "  +str(self.quantity)
        return data
