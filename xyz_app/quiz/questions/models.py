from django.contrib.postgres.fields import ArrayField
from django.db import models
from ..common.models import CommonFields
from ..kategoriler.models import Kategori


class Question(CommonFields):
    question = models.TextField()
    answer = ArrayField(models.TextField())
    rightAnswer = models.TextField()
    category = models.ForeignKey("Kategori", on_delete=models.CASCADE)
    DIFFICULTY_CHOICES = (
        ('Easy', 'easy'),
        ('Medium', 'medium'),
        ('Hard', 'hard'),
        ('Very Hard', 'very hard'),
        )
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default="medium")
