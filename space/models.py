from django.db import models
from django.utils import timezone   
from django.contrib.auth.models import User


class Fotografia(models.Model):

    categoria_choices = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"), 
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=categoria_choices, default="")
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateField(default=timezone.now, blank=False)
    usuario = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True, related_name="user",)


    def __str__(self) :
        return self.nome

