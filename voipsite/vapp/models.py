# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User



#Your phone numbers object
class NumObject(models.Model):
	
	title= models.CharField(max_length=50)
	number= models.IntegerField()
	ident= models.IntegerField()
	usersave= models.CharField(max_length=100, blank= True)


	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		super(NumObject,self).save(*args,**kwargs)

	def get_absolute_url(self):
		return reverse('posts:detail', kwargs={'id': self.id})


#sounds object
class Sounds(models.Model):
	numobj = models.ForeignKey(NumObject)
	title = models.CharField(max_length=50)
	sound = models.FileField()
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('posts:detail', kwargs={'title': self.title})




#incoming numbers model
class BlackList(models.Model):
	numkey = models.ForeignKey(NumObject)
	bnum = models.IntegerField(null= True)
	blocked = models.BooleanField(default=False)
	# days = models.CharField(max_length=(7*3))
	
	sun = models.BooleanField(default=False)
	mon = models.BooleanField(default=False)
	tue = models.BooleanField(default=False)
	wed = models.BooleanField(default=False)
	thurs = models.BooleanField(default=False)
	fri = models.BooleanField(default=False)
	sat = models.BooleanField(default=False)
	# sound = models.OneToOneField()

