from django.db import models


class Student(models.Model):
    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100, default='')
    data_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_ingresso = models.DateField()

    def __str__(self):
        return self.matricula
