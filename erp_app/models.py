from django.db import models

# Create your models here.

class Customer(models.Model):
    title = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    suffix = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=2000)
    display_name = models.CharField(max_length=200, blank=True)
    print_on_check_as = models.CharField(max_length=200, blank=True)
    billing_street = models.CharField(max_length=200, blank=True)
    billing_city = models.CharField(max_length=200, blank=True)
    billing_state = models.CharField(max_length=2, blank=True)
    billing_zip = models.CharField(max_length=10, blank=True)
    billing_country = models.CharField(max_length=200, blank=True) 
    shipping_street = models.CharField(max_length=200, blank=True)
    shipping_city = models.CharField(max_length=200, blank=True)
    shipping_state = models.CharField(max_length=2, blank=True)
    shipping_zip = models.CharField(max_length=10, blank=True)
    shipping_country = models.CharField(max_length=200, blank=True)   
    other_details = models.CharField(max_length=500, blank=True)
    
    def __unicode__(self):
      return self.company
   

class General_Setting(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

class Order(models.Model):
    cust_id = models.ForeignKey(Customer)
    invoice_creation_date = models.DateTimeField('Invoice Created Date')
    delivery_due_date = models.DateTimeField('Delivery Due Date')
    payment_due_date = models.DateTimeField('Payment Due Date') 
    custom_message = models.TextField()

    def __unicode__(self):
      return self.custom_message

class Product(models.Model):
    name = models.CharField(max_length=500) 
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __unicode__(self):
      return self.name

class Orders_Product(models.Model):
    order_id = models.ForeignKey(Order)
    product_id = models.ForeignKey(Product)
    quantity = models.IntegerField(default=0)


