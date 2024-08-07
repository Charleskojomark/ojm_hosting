from django.db import models
from userauth.models import User
# Create your models here.


RATINGS = (
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★"),
)


class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    service_description = models.TextField()
    additional_files = models.FileField(upload_to='additional_files/', blank=True, null=True)
    job_start = models.CharField(max_length=20, blank=True, null=True)
    readiness = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pros_contacted = models.IntegerField(default=0, null=True,blank=True)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.query
    
class Quote(models.Model):
    PRICE_TYPE_CHOICES = [
        ('Negotiable', 'Negotiable'),
        ('Fixed Price', 'Fixed Price'),
        ('Starting Fee', 'Starting Fee'),
        ('Per hour', 'Per hour'),
    ]
    
    request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    electrician = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_type = models.CharField(max_length=50, choices=PRICE_TYPE_CHOICES)
    price_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quote by {self.electrician.username} for {self.request.query}"

    
class Notification(models.Model):
    TYPE_CHOICES = [
        ('payment', 'Payment'),
        ('account', 'Account'),
        ('chat', 'Chat'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return f"{self.get_notification_type_display()} Notification for {self.user}"
    

class ServiceCategory(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"
        
class ServiceSubCategory(models.Model):
    category = models.ForeignKey(ServiceCategory, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    image = models.ImageField(upload_to='subcategory_images/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Service Subcategory"
        verbose_name_plural = "Service Subcategories"
    

class Service(models.Model):
    subcategory = models.ForeignKey(ServiceSubCategory, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,blank=True,null=True)
    short_description = models.TextField()
    recommended = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    image = models.ImageField(upload_to='service_images/')
    cover_image = models.ImageField(upload_to='cover_images/')
    
    note_to_customer = models.TextField()
    rating = models.IntegerField(choices=RATINGS, default=None)

    def discount_percent(self):
        if self.original_price > 0:
            discount = self.original_price - self.price
            return (discount / self.original_price) * 100
        return 0

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class Advertisement(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='advertisements/')

    def __str__(self):
        return self.name
    
    
class CustomerReviews(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    customer_image = models.ImageField(upload_to='customer_review_images/')
    customer_occupation = models.CharField(max_length=100,null=True,blank=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATINGS,default=None)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Customer Reviews"