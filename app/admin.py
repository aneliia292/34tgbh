from django.contrib import admin
from .models import *


class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date']
    list_display_links = ['id', 'title']
    list_filter = ['title', 'date']
    search_fields = ['title']


admin.site.register(Posts, PostsAdmin)
admin.site.register(Category)
admin.site.register(Likes)
admin.site.register(Comments)
admin.site.register(Image)
