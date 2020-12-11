from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from easy_thumbnails.fields import ThumbnailerImageField

class User(AbstractUser):
    modified_at = models.DateTimeField(auto_now=True, db_index=True)

    def avatar_path(self, filename):
        return os.path.join('user', str(self.id), 'profile{}'.format(os.path.splitext(filename)[1]))

    avatar = ThumbnailerImageField(upload_to=avatar_path, blank=True, null=True)

class BaseAccountModel(models.Model):
    added_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True

BAN_STATUSES = (
    ('temp', 'Temporary'),
    ('perm', 'Permanent'),
)

class Ban(BaseAccountModel):
    banned_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True, db_index=True, related_name='ban')
    banned_by_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='banned_users')
    ban_status = models.CharField(max_length=50, choices=BAN_STATUSES)
    ban_at = models.DateTimeField(default=timezone.now)
