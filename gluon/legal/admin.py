from django.contrib import admin

from .models import Entity, Person, Profile, Address

admin.register(Entity, Person, Profile, Address)
