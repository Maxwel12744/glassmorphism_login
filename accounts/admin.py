from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "last_login", "created_at")
    search_fields = ("user__username", "phone")

    def last_login(self, obj):
        return obj.user.last_login

    last_login.admin_order_field = "user__last_login"  # makes the column sortable


class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("last_login",)


# Swap Django's default User admin for the version with the extra column
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)