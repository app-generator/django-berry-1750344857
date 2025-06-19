# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    balance = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Vpnaccount(models.Model):

    #__Vpnaccount_FIELDS__
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=True, blank=True)
    protocol = models.CharField(max_length=255, null=True, blank=True)
    server_ip = models.CharField(max_length=255, null=True, blank=True)
    port = models.IntegerField(null=True, blank=True)
    uuid = models.CharField(max_length=255, null=True, blank=True)
    duration_days = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    expired_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    is_active = models.BooleanField()

    #__Vpnaccount_FIELDS__END

    class Meta:
        verbose_name        = _("Vpnaccount")
        verbose_name_plural = _("Vpnaccount")


class User(models.Model):

    #__User_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    balance = models.IntegerField(null=True, blank=True)
    is_reseller = models.BooleanField()
    password = models.CharField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Server(models.Model):

    #__Server_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    ip_address = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Server_FIELDS__END

    class Meta:
        verbose_name        = _("Server")
        verbose_name_plural = _("Server")


class Transaction(models.Model):

    #__Transaction_FIELDS__
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)
    method = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    proof_url = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Transaction_FIELDS__END

    class Meta:
        verbose_name        = _("Transaction")
        verbose_name_plural = _("Transaction")



#__MODELS__END
