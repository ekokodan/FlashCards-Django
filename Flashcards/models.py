from django.db import models

# Create your models here.

class Phrases(models.Model):
    English = models.CharField(max_length=500)
    French = models.CharField(max_length=500)
    Tenses = models.CharField(max_length=500)

    def __str__(self):
        return self.French + ' (Tense: ' + self.Tenses + ')'






class Word(models.Model):
    English = models.CharField(max_length=500)
    French = models.CharField(max_length=500)
    Tenses = models.CharField(max_length=500)

    def __str__(self):
        return self.French + ' (Tense: ' + self.Tenses + ')'


