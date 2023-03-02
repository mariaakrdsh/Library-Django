from django.contrib import admin

from .models import Order

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_name', 'user_name']
    search_fields = ['book__name', 'user__first_name', 'user__last_name']
    list_filter = ['book__name', 'user__first_name', 'user__last_name']

    def book_name(self, obj):
        return obj.book.name

    book_name.short_description = 'Book Name'

    def user_name(self, obj):
        return obj.user.first_name + " " + obj.user.last_name

    user_name.short_description = 'User Name'

admin.site.register(Order, CustomUserAdmin)