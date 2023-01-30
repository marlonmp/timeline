from uuid import uuid4

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin


class Manager(UserManager):

    def _create_user(self, username, email, password, **extra_fields):
        extra_fields.pop('is_staff')
        extra_fields.pop('is_superuser')
        return super()._create_user(username, email, password, **extra_fields)


# class User(AbstractBaseUser, PermissionsMixin):
class User(AbstractBaseUser):

    STATUS_UNVERIFIED = 'UF'
    STATUS_ACTIVE = 'AC'
    STATUS_DISABLED = 'DS'
    STATUS_DELETED = 'DL'

    CHOICE_STATUS = (
        (STATUS_UNVERIFIED, 'Unverified'),
        (STATUS_ACTIVE, 'Active'),
        (STATUS_DISABLED, 'Disabled'),
        (STATUS_DELETED, 'Deleted'),
    )

    GROUP_ADMIN = 'AD'
    GROUP_ACCOUNT_MANAGER = 'AM'
    GROUP_LEADER = 'LD'
    GROUP_DEVELOPER = 'DV'

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('nickname', 'email')

    uuid = models.UUIDField(unique=True, editable=False, default=uuid4)

    username = models.CharField(max_length=150, unique=True)

    nickname = models.CharField(max_length=150)

    email = models.EmailField(unique=True)

    status = models.CharField(max_length=2, choices=CHOICE_STATUS, default=STATUS_UNVERIFIED)

    created_at = models.DateTimeField(editable=False, auto_now_add=True)

    objects = Manager()

    @property
    def is_active(self):
        return self.status == self.STATUS_ACTIVE

    @property
    def is_staff(self):
        return self.status == self.STATUS_ACTIVE

    @property
    def is_superuser(self):
        return False
