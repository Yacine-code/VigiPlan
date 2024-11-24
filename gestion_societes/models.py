from django.db import models
from gestion_utilisateurs.models import CustomUser

class Société(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    administrateur = models.OneToOneField(
        CustomUser, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="societe"
    )

    def __str__(self):
        return self.nom

    def clean(self):
        if self.administrateur and Société.objects.exclude(pk=self.pk).filter(administrateur=self.administrateur).exists():
            raise ValidationError("Cet administrateur est déjà associé à une autre société.")
