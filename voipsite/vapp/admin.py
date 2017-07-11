# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import NumObject

class PlaceAdmin(admin.ModelAdmin):
	list_display = ('title', 'usersave')

admin.site.register(NumObject, PlaceAdmin)

# Register your models here.
