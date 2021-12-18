from django.contrib import admin

# Register your models here.
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    # list_display = ('id', 'name')
    print('hello ')


admin.site.register(Genre, GenreAdmin),
admin.site.register(Movie, MovieAdmin)
