# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class NumObject(models.Model):
	title= models.CharField(max_length=50)
	number= models.IntegerField()
	ident= models.IntegerField()
	sound= models.FileField()
	usersave= models.CharField(max_length=100, blank= True)


	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		super(NumObject,self).save(*args,**kwargs)

	def get_absolute_url(self):
		return reverse('posts:detail', kwargs={'id': self.id})

# Create your models here.
