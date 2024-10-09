from django.contrib import admin
from .models import UserRegistration

# Register your models here.
@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address', 'mobile', 'username')
    search_fields = ('first_name', 'last_name', 'username', 'email_address')
    ordering = ('last_name', 'first_name')