from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, login_name, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not login_name:
            raise ValueError(_('Users must have an login'))

        user = self.model(
            login_name=login_name,
            email=self.normalize_email(email),

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login_name, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            login_name,
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    login_name = models.CharField(
        verbose_name=_('user login'),
        max_length=32,
        unique=True,
    )
    first_name = models.CharField(
        verbose_name=_('First Name User'),
        max_length=64,
    )
    midle_name = models.CharField(
        verbose_name=_('Midle Name User'),
        max_length=64,
    )
    last_name= models.CharField(
        verbose_name=_('Last Name User'),
        max_length=64,
    )
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=64,
        unique=True,
    )
    departament = models.CharField(
        verbose_name=_('Organizational Unit Name (eg, section)'),
        max_length=64,
    )
    organisation = models.CharField(
        verbose_name=_('Organization Name (eg, company)'),
        max_length=64,
        default=_('Consultant ltd.'),
    )
    city = models.CharField(
        verbose_name=_('Locality Name (eg, city)'),
        max_length=64,
        default=_('Tomsk city'),
    )
    state = models.CharField(
        verbose_name=_('State or Province Name (full name)'),
        max_length=64,
        default=_('70 Tomsk region'),
    )
    RUSSIAN = 'RU'
    ENGLAND = 'UK'
    USA = 'US'

    COUNTRY_CHOISE = (
        (RUSSIAN, _('Russian')),
        (ENGLAND, _('GB Great Britain')),
        (USA, _('United States of America')),
    )




    country = models.CharField(
        verbose_name = _('Country Name'),
        max_length = 2,
        choices = COUNTRY_CHOISE,
        default = RUSSIAN,
    )



    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'login_name'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        # The user is identified by their email address
        return self.last_name + ' ' + self.first_name + ' ' + self.midle_name

    def get_short_name(self):
        # The user is identified by their email address

        if self.first_name != '' and self.midle_name != '' and self.last_name != '':
            return self.last_name + ' ' + self.first_name[0] + '.' + self.midle_name[0] + '.'
        else:
            return self.login_name

    def __str__(self):  # __unicode__ on Python 2
        return self.login_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
