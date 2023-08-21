from django.db import models

class Url(models.Model):
    source = models.URLField(unique=True)

    def __str__(self):
        return self.source