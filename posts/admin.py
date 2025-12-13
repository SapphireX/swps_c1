from django.contrib import admin
from .models import Category, Topic, Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("title", "topic","slug","created_by")
    list_display_links = ("title")

# Register your models here.
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Post, PostAdmin)
