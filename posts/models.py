from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, default='')

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']  # Sortowanie alfabetyczne po nazwie

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']  # Sortowanie alfabetyczne po nazwie

    def __str__(self):
        return self.name


class Post(models.Model):
    # Pole 1: Tytuł artykułu (krótki tekst, max 150 znaków)
    title = models.CharField(max_length=150)
    # Pole 2: Treść artykułu (długi tekst, bez limitu)
    text = models.TextField()
    # Pole 3: Relacja do Topic (klucz obcy, usuwanie kaskadowe)   
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # Pole 4: Slug - przyjazny URL (np. "moj-pierwszy-post")    
    slug = models.SlugField(unique=True, max_length=200)
    # Pole 5: Data utworzenia (automatycznie przy tworzeniu)  
    created_at = models.DateTimeField(auto_now_add=True)
    # Pole 6: Data ostatniej aktualizacji (automatycznie przy każdej zmianie)
    updated_at = models.DateTimeField(auto_now=True)
    # Pole 7: Autor artykułu (klucz obcy do User)
    # on_delete=models.SET_NULL = jeśli usuniesz User, ustaw NULL (nie usuwaj Post)
    # null=True, blank=True = pole może być puste
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']  # Sortuj od najnowszych

    def __str__(self):
        # Zwróć pierwsze 5 wyrazów tekstu + '...' jeżeli dłuższy
        words = self.text.split()
        if len(words) <= 5:
            return ' '.join(words)
        else:
            return ' '.join(words[:5]) + ' ...'  