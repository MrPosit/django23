from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    birthday = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name='Адрес', null=True, blank=True)
    picture = models.ImageField(upload_to='profile_pics', verbose_name='Аватар', null=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True, verbose_name='Возраст')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Телефон')

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.userprofile.save()
    except UserProfile.DoesNotExist:
        UserProfile.objects.create(user=instance)
