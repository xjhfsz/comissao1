from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em',
        auto_now=False,
        auto_now_add=True,
        )
    modified = models.DateTimeField(
        'modificado em',
        auto_now= True,
        auto_now_add=False,
    )

    class Meta:
        abstract = True
