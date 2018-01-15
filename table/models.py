from django.db import models


class Entry(models.Model):
    date = models.DateTimeField()
    filename = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    def __str__(self):
        return self.choice_text
    