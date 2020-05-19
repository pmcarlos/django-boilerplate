from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    """TimeStamped model."""
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class."""
        abstract = True


class User(BaseModel, AbstractUser):
    """Extend base Dajngo User model."""
