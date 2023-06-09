from django.db import models
from django.contrib.auth.hashers import make_password

class Cadastro(models.Model):
    login = models.CharField(max_length=50)
    senha = make_password(models.CharField(max_length=50))

    def __str__(self) -> str:
        return self.login