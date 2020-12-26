from django.contrib import admin
from .quiz.models import Question, Kategori

admin.site.register(Question)
admin.site.register(Kategori)