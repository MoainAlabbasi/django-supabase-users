from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    إعدادات لوحة الإدارة لنموذج المستخدم
    """
    list_display = ('id', 'username', 'email', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('username', 'email')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
