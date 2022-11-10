from django.db import models


class Boardgame(models.Model):
    name = models.CharField(max_length=300)
    producer = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    issue_year = models.CharField(max_length=10)
    min_age = models.PositiveSmallIntegerField()
    min_number_of_players = models.PositiveSmallIntegerField()
    max_number_of_players = models.PositiveSmallIntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name
