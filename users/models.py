from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

USER_ROLES = (
    ("1", "admin"),
    ("2", "moderator"),
    ("3", "user"),
)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/users/<id>/<filename> 
    return 'users/{0}/{1}'.format(instance.user.id, filename) 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=12, blank=True, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True)
    mobile = models.CharField(max_length=30, blank=True)
    birthday = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    role = models.CharField(max_length=20, choices=USER_ROLES, default="3")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code
    

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):    
    if created:
        profile, added = Profile.objects.get_or_create(code=instance.username)
        profile.user=instance
    instance.profile.save()