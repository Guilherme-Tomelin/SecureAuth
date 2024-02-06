from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    location = models.CharField(max_length=100, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    about_me = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.username