from django.db import models


# Create your models here.

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.topic_name


class WebPage(models.Model):
    category = models.ForeignKey(Topic, on_delete=None)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecords(models.Model):
    name = models.ForeignKey(WebPage, on_delete=None)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
