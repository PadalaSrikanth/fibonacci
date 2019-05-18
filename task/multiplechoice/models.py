from django.db import models


class Track(models.Model):
    track_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)

    def __str__(self):
        return str(self.track_id)


class Question(models.Model):
    track = models.ForeignKey(Track, null=True, on_delete=models.CASCADE)
    ques_id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length = 1000)

    def __str__(self):
        return str(self.ques_id)


class Choices(models.Model):
    choice = models.CharField(max_length=250)
    votes = models.IntegerField()
    ans = models.BooleanField(default=False)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice
