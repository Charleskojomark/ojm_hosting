from django.contrib import admin
from .models import ServiceRequest, Notification,Quote,Service,ServiceCategory,ServiceSubCategory,Advertisement
admin.site.register(ServiceRequest)
admin.site.register(Notification)
admin.site.register(Quote)
admin.site.register(Service)
admin.site.register(ServiceCategory)
admin.site.register(ServiceSubCategory)
admin.site.register(Advertisement)