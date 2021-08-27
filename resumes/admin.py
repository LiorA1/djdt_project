from django.contrib import admin

# Register your models here.

from .models import Resume, Review, Tag

admin.site.register(Resume)
admin.site.register(Review)
admin.site.register(Tag)
