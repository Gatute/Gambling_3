from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a PerfilUsuario for the new user
        PerfilUsuario.objects.create(user=instance)
    else:
        # Ensure the PerfilUsuario exists for existing users
        if not hasattr(instance, 'perfilusuario'):
            PerfilUsuario.objects.create(user=instance)