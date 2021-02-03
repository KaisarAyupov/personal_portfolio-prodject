from django.db import models
import readtime


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def get_readtime(self):
        result = readtime.of_text(self.description)
        return result.text

    def __str__(self):
        return self.title
