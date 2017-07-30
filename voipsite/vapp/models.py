# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from datetime import time 



#User phone numbers object
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

	#TOP LEVEL FIELDS 
	numkey = models.ForeignKey(NumObject)
	bnum = models.IntegerField(null= True)
	blocked = models.BooleanField(default=False)
	



	BLOCKED_TIMES_BEGIN = (
		(time(0,0),'12 AM'),
		(time(1,0),'1 AM'),
		(time(2,0),'2 AM'),
		(time(3,0),'3 AM'),
		(time(4,0),'4 AM'),
		(time(5,0),'5 AM'),
		(time(6,0),'6 AM'),
		(time(7,0),'7 AM'),
		(time(8,0),'8 AM'),
		(time(9,0),'9 AM'),
		(time(10,0),'10 AM'),
		(time(11,0),'11 AM'),
		(time(12,0),'12 PM'),

		)

	BLOCKED_TIMES_END = (
		(time(0,0),'12 AM'),
		(time(1,0),'1 AM'),
		(time(2,0),'2 AM'),
		(time(3,0),'3 AM'),
		(time(4,0),'4 AM'),
		(time(5,0),'5 AM'),
		(time(6,0),'6 AM'),
		(time(7,0),'7 AM'),
		(time(8,0),'8 AM'),
		(time(9,0),'9 AM'),
		(time(10,0),'10 AM'),
		(time(11,0),'11 AM'),
		(time(12,0),'12 PM'),

		)

	# START/END TIME FOR EACH DAY
	sun_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True)
	sun_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True)

	sun_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True)
	sun_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True)

	mon_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True)
	mon_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True)

	tue_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True)
	tue_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True)

	wed_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True)
	wed_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True)

	thu_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True)
	thu_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True)

	fri_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True)
	fri_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True)

	sat_begin_time= models.TimeField(choices=BLOCKED_TIMES_BEGIN, null=True)
	sat_end_time= models.TimeField(choices= BLOCKED_TIMES_END,null=True)

	# DAYS CHECKED
	sun = models.BooleanField(default=False)
	mon = models.BooleanField(default=False)
	tue = models.BooleanField(default=False)
	wed = models.BooleanField(default=False)
	thu = models.BooleanField(default=False)
	fri = models.BooleanField(default=False)
	sat = models.BooleanField(default=False)


	# sound = models.OneToOneField()

