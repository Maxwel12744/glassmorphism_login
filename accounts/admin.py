
# Register your models here.
from django.contrib import admin
from .models import Profile


@admin.register(Profile)  # makes Profile appear in the admin site
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "created_at")  # columns in the list page
    search_fields = ("user__username", "phone")     # adds a search box