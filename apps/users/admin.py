from django.contrib import admin

from apps.users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'date_joined']
