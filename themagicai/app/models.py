from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Skill(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name


class Letter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()


class PostCV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.user.username
