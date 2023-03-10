from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Skill(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Letter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    requirement = models.TextField()
    skills = models.ManyToManyField(Skill)
    about = models.TextField()
    result = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.name} {self.company}"


class PostCV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    requirement = models.TextField()
    skills = models.ManyToManyField(Skill)
    about = models.TextField()
    result = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.name} {self.company}"
