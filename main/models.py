from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class MainPost(models.Model):
    user = models.ForeignKey(User, related_name="main_posts", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} ({self.created_at:%Y-%m-%d %H:%M}): {self.body}..."

    class Meta:
        verbose_name = "Main Post"
        verbose_name_plural = "Main Posts"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg', blank=True)
    date_modified = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)  
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

#post_save.connect(create_profile, sender=User)