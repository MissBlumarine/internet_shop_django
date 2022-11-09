from django.db import models


class BoardgameAge(models.Model):
    age = models.CharField(max_length=2)

    def __str__(self):
        return self.age


class Addition(models.Model):
    name = models.CharField(max_length=300)
    producer = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    issue_year = models.CharField(max_length=10)
    min_age_of_player = models.ForeignKey(BoardgameAge, on_delete=models.PROTECT)
    min_number_of_players = models.PositiveSmallIntegerField()
    max_number_of_players = models.PositiveSmallIntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Boardgame(models.Model):
    name = models.CharField(max_length=300)
    producer = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    issue_year = models.CharField(max_length=10)
    min_age_of_player = models.ForeignKey(BoardgameAge, on_delete=models.PROTECT, related_name="boardgame")
    min_number_of_players = models.PositiveSmallIntegerField()
    max_number_of_players = models.PositiveSmallIntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # addition = models.ForeignKey(Addition, on_delete=models.PROTECT)

    def __str__(self):
        return self.name






