# Rozwiązania zadań lab 5

## Zadanie 1
Uruchom Django shell i dodaj po 3 nowe obiekty typu Category, Topic oraz Post.

```python
# Uruchomienie Django shell
# python manage.py shell

from posts.models import Category, Topic, Post
from django.contrib.auth.models import User

# Dodanie 3 kategorii
cat1 = Category.objects.create(name="Filmy", description="Kategoria filmowa")
cat2 = Category.objects.create(name="Muzyka", description="Kategoria muzyczna")
cat3 = Category.objects.create(name="Sport", description="Kategoria sportowa")

# Dodanie 3 topików
topic1 = Topic.objects.create(name="Batman", category=cat1)
topic2 = Topic.objects.create(name="Rock", category=cat2)
topic3 = Topic.objects.create(name="Piłka nożna", category=cat3)

# Pobranie użytkownika (lub stworzenie nowego)
user = User.objects.first()  # lub User.objects.get(username='admin')

# Dodanie 3 postów
post1 = Post.objects.create(
    title="Pierwszy post o Batmanie",
    text="To jest mój pierwszy post o Batmanie. Batman jest superbohaterem z Gotham City.",
    topic=topic1,
    slug="pierwszy-post-o-batmanie",
    created_by=user
)

post2 = Post.objects.create(
    title="Najlepsze zespoły rockowe",
    text="Rock to gatunek muzyczny który powstał w latach pięćdziesiątych dwudziestego wieku.",
    topic=topic2,
    slug="najlepsze-zespoly-rockowe",
    created_by=user
)

post3 = Post.objects.create(
    title="Mundial 2026",
    text="Mistrzostwa świata w piłce nożnej odbędą się w Stanach Zjednoczonych Meksyku i Kanadzie.",
    topic=topic3,
    slug="mundial-2026",
    created_by=user
)
```

## Zadanie 2
Wykonaj zapytanie filtrujące obiekty typu Topic, których nazwa rozpoczyna się od wybranej przez Ciebie litery.

```python
# Filtrowanie topików zaczynających się na literę 'B'
Topic.objects.filter(name__startswith='B')

# lub na literę 'P'
Topic.objects.filter(name__startswith='P')

# lub na literę 'R'
Topic.objects.filter(name__startswith='R')
```

## Zadanie 3
Dla danych zwróconych w zadaniu 2 wyświetl listę wszystkich wartości tych obiektów (metoda values()).

```python
# Wyświetlenie wartości dla topików zaczynających się na 'B'
Topic.objects.filter(name__startswith='B').values()

# lub dla innej litery, np. 'P'
Topic.objects.filter(name__startswith='P').values()
```

## Zadanie 4
Wykonaj pobranie wszystkich obiektów typu Post i zapisz to do zmiennej posts.

```python
# Pobranie wszystkich postów
posts = Post.objects.all()
```

## Zadanie 5
Z listy stworzonej w zadaniu 4 za pomocą cięcia (slicing) wyświetl:
- pierwszy element,
- ostatni element,
- wszystkie elementy w odwróconej kolejności (od ostatniego do pierwszego),
- co drugi element.

```python
# Pierwszy element
posts[0]

# Ostatni element
posts.last()
# lub alternatywnie
posts[posts.count()-1]

# Wszystkie elementy w odwróconej kolejności
posts.reverse()
# lub alternatywnie
Post.objects.all().order_by('-created_at')

# Co drugi element
posts[::2]
```

## Zadanie 6
Wyświetl wszystkie topiki sortując po nazwie w porządku alfabetycznym od Z do A.

```python
# Sortowanie od Z do A (malejąco)
Topic.objects.all().order_by('-name')
```

## Zadanie 7
Wyświetl wszystkie obiekty Topic, których id jest mniejsze niż 3 używając metody exclude().

```python
# Exclude wyklucza warunki - aby pokazać id < 3, wykluczamy id >= 3
Topic.objects.exclude(id__gte=3)
# lub alternatywnie (wykluczamy id > 2, co daje nam id <= 2, czyli id < 3)
Topic.objects.exclude(id__gt=2)
```
