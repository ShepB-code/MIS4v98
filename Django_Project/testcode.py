import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'learning_log.settings')


import django
django.setup()

from MainApp.models import Topic


topics = Topic.objects.all()

for t in topics:
    print(f'ID: {t.id}, Name: {t.text}')


t = Topic.objects.get(id=1)
print(t.date_added)
