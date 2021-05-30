# E Commerce Project
  
 Problem Statement: Create an Online Shopping Website
  
## Requirements ##

 - Python 
 - Django
 
_It is advised to install django in a virtual mwrapper to keep the files seperate. You can do this by using a virtual environment wrapper. Here's a [tutorial](https://www.youtube.com/watch?v=VuETrwKYLTM&t=10s") about setting up Django & Virtual Wrapper._

## Installation ##

Clone this repo or download the code as zip file and extract it.

## Issue ## 
 This is the home page of our project:
 ![picture alt](https://pic8.co/sh/puoHti.png)
 
 If you click on the cart icon on the navbar, it should lead you to the cart system but it displays an error
![picture alt](https://pic8.co/sh/yDfUBN.png)
![Screenshot (293)](https://user-images.githubusercontent.com/64654648/120106970-b6170700-c17c-11eb-85bc-52629d699cc1.png)


The issue is in the file models.py. Here's a code snippet of class where I feel the problem could be:
``` 
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    digital = models.BooleanField(default=False,null=True, blank=True)  #To check of a product is a virtual  product or physical product.
    image = models.ImageField(null=True, blank=True)
    is_this_a_local_product = models.BooleanField(default=True,null=True, blank=True)  #To check of a product is a virtual  product or physical product.
    
    def __str__(self):
        return self.name
    

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url
        
class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
```
Let me know if you know the solution to this problem. And feel free to explore the code to search the cause of the error. Thank you!
