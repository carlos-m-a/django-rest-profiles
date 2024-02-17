from django.db import models
from django.conf import settings

class CountryPhoneCode(models.Model):
    code = models.CharField(
        blank=True, 
        max_length=8, 
        null=True
    )

    def __str__(self):
        return self.code


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=False, 
        related_name='profile'
    )
    is_verified = models.BooleanField(
        null=False, 
        default=False
    )
    is_private = models.BooleanField(
        null=False, 
        default=False
    )
    date_of_birth = models.DateField(
        null=True, 
        blank=True
    )
    sex_or_genre = models.PositiveSmallIntegerField(
        null=False, 
        default=1
    )
    avatar_image = models.ImageField(
        upload_to='images/', 
        null=True, 
        blank=True, 
        max_length=254
    )
    description_text = models.CharField(
        blank=True, 
        max_length=254, 
        null=True
    )
    # Inside organizations, normally users has a organization id, different from database id
    other_id = models.CharField(
        blank=True, 
        max_length=128, 
        null=True
    )
    phone_number = models.CharField(
        blank=True, 
        max_length=20, 
        null=True
    )
    country_phone_code = models.ForeignKey(
        CountryPhoneCode,
        on_delete=models.CASCADE,
        null=True
    )
    is_phone_number_verified = models.BooleanField(
        null=False, 
        default=False
    )

    def __str__(self):
        return self.user.username


class Setting(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        null=False, 
        related_name='setting'
    )
    # Dark or light theme, for example
    frontend_theme = models.PositiveSmallIntegerField(
        null=False, 
        default=1
    )
    language = models.PositiveSmallIntegerField(
        null=False, 
        default=1
    )
    time_zone = models.PositiveSmallIntegerField(
        null=False, 
        default=1
    )
    date_format = models.PositiveSmallIntegerField(
        null=False, 
        default=1
    )

    def __str__(self):
        return self.user.username