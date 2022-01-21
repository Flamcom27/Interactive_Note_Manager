from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)

    def __repr__(self):
        return self.title


class Term(models.Model):
    title = models.CharField(max_length=50)
    definition = models.TextField()
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __repr__(self):
        return self.title
