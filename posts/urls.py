from django.urls import path

# importujemy moduł views (plik views.py z tego samego katalogu co plik bieżący)
from . import views

# definiujemy zmienną urlpatterns, która jest listą mapowań adresów URL na nasze widoki
urlpatterns = [
    path("welcome", views.welcome_view),
    path("topics", views.topic_list),
    path("topics/<int:id>/posts", views.topic_posts),
    path("topics/<int:id>", views.topic_detail),
    path("categories", views.category_list),
    path("categories/<int:id>", views.category_detail),
    path("posts", views.post_list),
    path("posts/<int:id>", views.post_detail),
]

