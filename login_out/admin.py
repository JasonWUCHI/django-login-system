from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput , Textarea
# Register your models here.

class UserAdminConfig(UserAdmin):
    model = User
    ordering = ('-timestamp')
    list_display = ('email' , 'username' , 'timestamp' , 'is_active' , 'is_staff')

class ProfileConfig(admin.ModelAdmin):
    model = Profile
    fieldsets = (
        ('Name', {
            'fields': ('first_name' , 'last_name' , 'prefer_name')
        }),
        ('Information', {
            'fields': ('gender' , 'school')
        })
    )



admin.site.register(User)
admin.site.register(Profile)