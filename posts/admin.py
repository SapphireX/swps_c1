from django.contrib import admin
from .models import Category, Topic, Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['title', 'short_post', 'topic_category_name', 'slug', 'created_by', 'created_at']
    list_display_links = ['title']
    list_filter = ['topic', 'topic__category', 'created_by', 'created_at']
    prepopulated_fields = {'slug': ['title']}

    @admin.display(description='Short post version')
    def short_post(self, obj):
        words = obj.text.split()
        if len(words) <= 5:
            return ' '.join(words)
        else:
            return ' '.join(words[:5]) + ' ...'

    @admin.display(description='Topic name (Category name)')
    def topic_category_name(self, obj):
        return f'{obj.topic.name} ({obj.topic.category.name})'


class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created']
    # można też pobrac tylko id kategorii bez zapytania do tabeli category o pozostale cechy
    # list_display = ['name', 'category_id', 'created']
    # category__name - to jest model category (nie klucz obcy category) oraz nazwa dla tabeli category o pozostale cechy
    # oraz cecha name - pozwala po nazwie dla topic (name) oraz
    # dla nazwy kategorii (category__name)
    search_fields = ['name', 'category__name']
    list_filter = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Category, CategoryAdmin)
