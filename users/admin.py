from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'date_joined',
        'date_berth',
    ]
    list_display_links = ['username']
    readonly_fields = ['image', 'date_joined']
    search_fields = ['username__icontains', 'first_name__icontains', 'last_name__icontains', 'email__icontains', ]
    list_per_page = 15
    list_editable = ['is_active']
    ordering = ['date_joined', 'username']
    list_filter = ['is_active', 'date_joined', 'date_berth', ]
    save_on_top = True
