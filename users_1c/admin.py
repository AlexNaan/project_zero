from django.contrib import admin
from .models import ListUsers
# Register your models here.

@admin.register(ListUsers)
class ListUsersAdmin(admin.ModelAdmin):
    list_display = ('name_users_1c','kod_users_1c','slug','user_web','created')
    list_filter = ('created','user_web')
    search_fields = ('name_users_1c','user_web')
    prepopulated_fields = {'slug': ('name_users_1c',)}
