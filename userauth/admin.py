from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User,ElectricianProfile,CustomerProfile,Identity
class ElectricianProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'business_name','get_phone_number','country', 'state', 'city')
    
    def get_phone_number(self, obj):
        return obj.user.phone_number
    get_phone_number.short_description = 'Phone Number'

class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('user','get_phone_number','country', 'state', 'city')
    
    def get_phone_number(self, obj):
        return obj.user.phone_number
    get_phone_number.short_description = 'Phone-Number'
    
class CustomUserAdmin(UserAdmin):
    # Define the list filters
    list_filter = ('is_active', 'groups')

    search_fields = ('username',)

    list_display = ('username', 'email','phone_number', 'first_name', 'last_name', 'is_active')

   

admin.site.register(Identity)
admin.site.register(ElectricianProfile, ElectricianProfileAdmin)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
admin.site.register(User, CustomUserAdmin)
