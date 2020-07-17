from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import GoGoManager
from django.core.validators import RegexValidator


class GoGoUser(AbstractUser):

    created_by = models.ForeignKey('self',on_delete=models.CASCADE,related_name="createdBy",null=True)
    modified_by = models.ForeignKey('self',on_delete=models.CASCADE,related_name="modifiedBy",null=True)
    date_modified = models.DateTimeField(null=True)
    secondary_email = models.TextField(blank=True,null=True)
    is_self_register = models.BooleanField(null=True)
    is_emergency = models.BooleanField(null=True)
    is_deleted = models.BooleanField(null=True)
    user_status = models.IntegerField(null=True)
    device_type = models.IntegerField(null=True)
    device_version = models.TextField(null=True)
    otp = models.TextField(null=True)
    login_date = models.DateTimeField(null=True)
    otp_verified = models.BooleanField(null=True)
    longitude = models.TextField(null=True)
    latitude = models.TextField(null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format: '9999999999'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10,null=True)
    gender = models.CharField(
        max_length=10,
        choices=(
            ('FEMALE', 'Female',),
            ('MALE', 'Male',),
            ('UNSURE', 'Unsure')),null=True
    )

    objects = GoGoManager()

    def __repr__(self):
        return str(self.username) + ' : ' + str(self.email)