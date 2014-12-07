from django.contrib import admin

from .models import Entity, Person, Profile, Address

admin.site.register(Entity)
admin.site.register(Person)
admin.site.register(Profile)
admin.site.register(Address)
