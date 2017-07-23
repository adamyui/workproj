# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .models import NumObject, Sounds
from .forms import PostForm, NumForm, BlacklistForm, AddRules
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView



#main wall displaying all your numbers
def index(request):
	
	listboy= NumObject.objects.all()
	
	context= {
		'object_listboy': listboy,
				
	}
	return render(request, 'wall.html', context)

#Your number detail 
def post_detail(request,id= None):
	instance= get_object_or_404(NumObject, id=id)
	form= AddRules(request.POST or None, request.FILES or None)
	incomingform= BlacklistForm(request.POST or None, request.FILES or None)

	if incomingform.is_valid():
		instanceIncoming = incomingform.save(commit=False)
		instanceIncoming.save()
		return redirect('posts:list')

	
	if form.is_valid():
		instancerules = form.save(commit=False)
		instancerules.save()
		return redirect('posts:list')
	
	context= {

		'incomingform': incomingform,
		'form' :form,
		'title': instance.number,
		'instance': instance,
		'numkey': instance.title,
		
	}
	return render(request,'post_detail.html',context)


def sound_detail(request,id= None):
	instance= get_object_or_404(Sounds, id=id)
	

	context= {		
		'instance': instance,
	}
	return render(request,'sound_detail.html',context)




#create incoming numbers form
# def blacklist_create(request):
# 	incomingform= BlacklistForm(request.POST or None, request.FILES or None)


# 	if form.is_valid():

# 		instance = form.save(commit=False)
# 		instance.save()
# 		return HttpResponseRedirect('/')

	
# 	context= {
# 		'form': form,
# 	}
# 	return render(request,'blacklist_form.html',context,)

#SOUND UPLOAD VIEW
def post_create(request):
	form= PostForm(request.POST or None, request.FILES or None)


	if form.is_valid():

		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect('/')

	
	context= {
		'form': form,
	}
	return render(request, 'post_form.html',context,)




#CREATE USER NUMBERS VIEW
def post_createnum(request):
	form= NumForm(request.POST or None, request.FILES or None)


	if form.is_valid():

		instance = form.save(commit=False)
		# instance.user = User.objects.get(user=self.request.user)
		instance.save()
		return HttpResponseRedirect('/')

	
	context= {
		'form': form,
	}
	return render(request, 'num_form.html',context)

#CREATE RULESET FORM	
def bl_createrules(request):
	form= AddRules(request.POST or None, request.FILES or None)


	if form.is_valid():

		instance = form.save(commit=False)
		# instance.user = User.objects.get(user=self.request.user)
		instance.save()
		return HttpResponseRedirect('/')

	
	context= {
		'form': form,
	}
	return render(request,'post_detail.html',context)


#DELETE SOUND VIEW
def post_delete(request, id):
	sound= get_object_or_404(Sounds, pk=id).delete()
	
	return redirect('posts:list')

