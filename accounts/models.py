
# Create your models here.
from django.db import models
from django.conf import settings


class Profile(models.Model):
    # Links each Profile to exactly one User (one user = one profile).
    # on_delete=CASCADE: if the user is deleted, their profile is deleted too.
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    # Extra details Django's User doesn't store.
    # blank=True means the field is optional.
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)

    # Filled in automatically with the date and time the profile is created.
    created_at = models.DateTimeField(auto_now_add=True)

    # What shows up in the admin list instead of "Profile object (1)".
    def __str__(self):
        return self.user.username