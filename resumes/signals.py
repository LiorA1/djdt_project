
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import Resume


@receiver(post_delete, sender=Resume)
def resume_post_delete_handler(sender, **kwargs):
    """signal which invalidate the cache, when a resume is deleted."""
    cache.clear()


@receiver(post_save, sender=Resume)
def resume_post_save_handler(sender, **kwargs):
    """signal which invalidate the cache, when a new resume is added."""
    cache.clear()


@receiver(post_delete, sender=Resume)
def resume_post_delete_handler(sender, instance, **kwargs):
    '''deletes the resume file from --'''
    if instance.resume_file:
        instance.resume_file.delete(save=False)
