from djongo import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100, blank=True, null=True)
    workouts = models.JSONField(default=list)
    activities = models.JSONField(default=list)
    leaderboard_score = models.IntegerField(default=0)
    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=150)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    calories = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user} - {self.type}"

class Leaderboard(models.Model):
    user = models.CharField(max_length=150)
    score = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.user}: {self.score}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    def __str__(self):
        return self.name
