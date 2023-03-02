from django.contrib import admin
from .models import Book
from author.models import Author

class AuthorListFilter(admin.SimpleListFilter):
    title = 'author surname'
    parameter_name = 'author_surname'

    def lookups(self, request, model_admin):
        authors = Author.objects.all()
        return [(author.surname, author.surname) for author in authors]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(authors__surname=self.value())
        return queryset


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'year_of_publication', 'date_of_issue', 'list_of_authors']
    search_fields = ['name', 'description', 'year_of_publication', 'date_of_issue']
    list_filter = ['name', 'description', AuthorListFilter, 'year_of_publication', 'date_of_issue']

    def list_of_authors(self, obj):
        return ", ".join([author.surname for author in obj.authors.all()])

    list_of_authors.short_description = 'Authors'

    fieldsets = [
        ('Basic information', {
            'fields': ['name', 'description', 'year_of_publication']
        }),
        ('Issue information', {
            'fields': ['date_of_issue']
        }),
    ]


admin.site.register(Book, BookAdmin)
