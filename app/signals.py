from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def notify_admin_on_user_creation(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Новый пользователь зарегистрирован',
            f'Пользователь {instance.username} зарегистрировался на сайте.',
            'admin@example.com',
            ['admin@example.com'],
            fail_silently=False,
        )