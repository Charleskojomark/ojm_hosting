from django.db import models
from userauth.models import User
# Create your models here.
class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    service_description = models.TextField()
    additional_files = models.FileField(upload_to='additional_files/', blank=True, null=True)
    job_start = models.CharField(max_length=20, blank=True, null=True)
    readiness = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
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
    
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    short_description = models.TextField()
    description = models.TextField()
    recommended = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)
    image = models.ImageField(upload_to='service_images/')
    cover_image = models.ImageField(upload_to='cover_images/')
    need_the_service = models.TextField()
    whats_included = models.TextField()
    whats_excluded = models.TextField()
    note_to_customer = models.TextField()

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
