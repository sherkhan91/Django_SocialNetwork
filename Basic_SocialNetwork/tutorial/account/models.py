# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import post_save
from django.db import models
#from django.db import models as myModel
from django.contrib.auth.models import User
# Create your models here.


class UserProfileManager(models.Manager):
	def get_queryset(self):
		return super(UserProfileManager, self).get_queryset().filter(city='London')


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=100, default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default='0')
	image = models.ImageField(upload_to='profile_image', blank=True)

	London = UserProfileManager()


	def __str__(self):
		return self.user.username


def create_profile(sender, **kwargs):
	if kwargs['created']:
		try:
			user_profile = UserProfile.objects.create(user=kwargs['instance'])
		except:
			user_profile = None	


post_save.connect(create_profile, sender=User)