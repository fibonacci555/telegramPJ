from django.db import models

# Create your models here.


class Inscricoes(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    phone = models.CharField(max_length=20, blank=False, null=False,unique=True)

    def __str__(self):
        return f'Nome: {self.nome} | Número: {self.phone} | Email: {self.email}'