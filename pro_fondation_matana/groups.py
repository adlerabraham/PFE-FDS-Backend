import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro_fondation_matana.settings')

import django

django.setup()
from django.contrib.auth.models import Group


GROUPS = ['superadmin', 'admin', 'teacher', 'student']
MODELS = ['user']

for group in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group)
    if created:
            print(f'{group} group created')
    else:
            print(f'{group} group already exists')    