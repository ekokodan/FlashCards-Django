from django.contrib import admin
from .models import Phrases
from .models import Word
# Register your models here.

admin.site.register(Phrases)
admin.site.register(Word)

