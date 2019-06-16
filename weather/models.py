from django.db import models


class City(models.Model):
    name = models.CharField(max_length=35)
    country = models.CharField(max_length=3)

    def __srt__(self):
        return self.name, self.country

