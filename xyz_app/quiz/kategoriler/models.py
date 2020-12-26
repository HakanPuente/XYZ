from django.db import models
from ..common.models import CommonFields


class Kategori(CommonFields):
    name = models.TextField()
    description = models.TextField()