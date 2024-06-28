from django.contrib import admin
from .models import Request, Notification,Quote,Service,ServiceCategory,ServiceSubCategory
admin.site.register(Request)
admin.site.register(Notification)
admin.site.register(Quote)
admin.site.register(Service)
admin.site.register(ServiceCategory)
admin.site.register(ServiceSubCategory)
