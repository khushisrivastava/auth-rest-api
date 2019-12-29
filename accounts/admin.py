from django.contrib import admin 
from accounts.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone') 
    list_display_links = ('id', 'username')
    search_fields = ('user_name', 'first_name', 'last_name')
    listing_per_page = 30

admin.site.register(User, UserAdmin)

