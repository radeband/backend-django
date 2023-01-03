from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from _helpers.models import BaseModel
from account.utils import OTPMixin
from account.validators import IranMobilePhoneNumberValidator


class User(BaseModel, AbstractUser, OTPMixin):
    mobile = models.CharField(max_length=20, unique=True)

    is_mobile_number_verified = models.BooleanField(default=False)

    username = None
    USERNAME_FIELD = "mobile"

    class Meta:
        db_table = 'users'
