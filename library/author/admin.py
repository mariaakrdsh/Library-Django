from .models import Author
from django.contrib import admin


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'patronymic']
    search_fields = ['name', 'surname', 'patronymic']
    list_filter = ['name', 'surname', 'patronymic']
    fieldsets = [('Author Information', {'fields': ['name', 'surname', 'patronymic']}),
                 ('Books Information', {'fields': ['books']}),
                 ]


admin.site.register(Author, AuthorAdmin)
