"""
Skrypt testowy dla serializerów Django REST Framework
Uruchom: python manage.py shell < test_serializers.py
"""

print("=" * 60)
print("TEST SERIALIZERÓW DLA LAB 7")
print("=" * 60)

from posts.serializers import CategorySerializer, TopicSerializer, PostSerializer
from posts.models import Category, Topic, Post
from django.contrib.auth.models import User

# ============================================================
# TEST 1: CategorySerializer (ModelSerializer)
# ============================================================
print("\n[TEST 1] CategorySerializer - CREATE")
print("-" * 60)

data = {'name': 'Python', 'description': 'Python programming tutorials'}
serializer = CategorySerializer(data=data)

if serializer.is_valid():
    category = serializer.save()
    print(f"✓ Category created: ID={category.id}, Name={category.name}")
    print(f"  Serialized data: {CategorySerializer(category).data}")
else:
    print(f"✗ Validation failed: {serializer.errors}")

# ============================================================
# TEST 2: TopicSerializer (Serializer z create/update)
# ============================================================
print("\n[TEST 2] TopicSerializer - CREATE")
print("-" * 60)

# Pobierz pierwszą kategorię (lub stwórz jeśli nie ma)
try:
    category = Category.objects.first()
    if not category:
        category = Category.objects.create(name='Django', description='Django framework')
        print(f"  Created test category: {category.name}")
except:
    print("✗ Error accessing Category model")
    category = None

if category:
    data = {'name': 'Django REST Framework', 'category': category.id}
    serializer = TopicSerializer(data=data)

    if serializer.is_valid():
        topic = serializer.save()
        print(f"✓ Topic created: ID={topic.id}, Name={topic.name}, Created={topic.created}")
        print(f"  Serialized data: {TopicSerializer(topic).data}")
    else:
        print(f"✗ Validation failed: {serializer.errors}")

# ============================================================
# TEST 3: TopicSerializer - UPDATE
# ============================================================
print("\n[TEST 3] TopicSerializer - UPDATE")
print("-" * 60)

try:
    topic = Topic.objects.first()
    if topic:
        data = {'name': 'Updated Topic Name', 'category': topic.category.id}
        serializer = TopicSerializer(topic, data=data)

        if serializer.is_valid():
            updated_topic = serializer.save()
            print(f"✓ Topic updated: Name={updated_topic.name}")
        else:
            print(f"✗ Validation failed: {serializer.errors}")
    else:
        print("  No topics available for update test")
except Exception as e:
    print(f"✗ Error: {e}")

# ============================================================
# TEST 4: PostSerializer (ModelSerializer)
# ============================================================
print("\n[TEST 4] PostSerializer - CREATE")
print("-" * 60)

try:
    topic = Topic.objects.first()
    if not topic:
        print("  No topic available, creating one...")
        category = Category.objects.first() or Category.objects.create(name='Test')
        topic = Topic.objects.create(name='Test Topic', category=category)

    data = {
        'title': 'My First DRF Post',
        'text': 'This is a test post created using Django REST Framework serializers.',
        'topic': topic.id,
        'slug': 'my-first-drf-post',
        'created_by': None  # nullable field
    }

    serializer = PostSerializer(data=data)

    if serializer.is_valid():
        post = serializer.save()
        print(f"✓ Post created: ID={post.id}, Title={post.title}")
        print(f"  Slug: {post.slug}")
        print(f"  Created at: {post.created_at}")
        print(f"  Serialized data:")
        for key, value in PostSerializer(post).data.items():
            print(f"    {key}: {value}")
    else:
        print(f"✗ Validation failed: {serializer.errors}")
except Exception as e:
    print(f"✗ Error: {e}")

# ============================================================
# TEST 5: Walidacja - brakujące pola
# ============================================================
print("\n[TEST 5] Walidacja - brakujące wymagane pola")
print("-" * 60)

serializer = PostSerializer(data={'title': 'Only title'})
print(f"  Is valid: {serializer.is_valid()}")
if not serializer.is_valid():
    print(f"  Errors: {serializer.errors}")

# ============================================================
# TEST 6: Lista obiektów (many=True)
# ============================================================
print("\n[TEST 6] Serializacja listy obiektów")
print("-" * 60)

categories = Category.objects.all()[:3]
serializer = CategorySerializer(categories, many=True)
print(f"✓ Serialized {len(serializer.data)} categories:")
for cat_data in serializer.data:
    print(f"  - {cat_data['name']}")

print("\n" + "=" * 60)
print("TESTY ZAKOŃCZONE")
print("=" * 60)
