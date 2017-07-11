# -*- coding: utf-8 -*-
from __future__ import unicode_literals



from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .models import NumObject
from .forms import PostForm





def index(request):
	
	listboy= NumObject.objects.all()
	context= {
		'object_listboy': listboy,
		
	}
	return render(request, 'wall.html', context)


def post_detail(request,id= None):
	instance= get_object_or_404(NumObject, id=id)

	context= {
		'title': instance.number,
		'instance': instance,
	}
	return render(request,'post_detail.html',context)




def post_create(request):
	form= PostForm(request.POST or None, request.FILES or None)


	if form.is_valid():

		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, 'Successfully Created')
		return HttpResponseRedirect('/')

	
	context= {
		'form': form,
	}
	return render(request, 'post_form.html',context,)


def post_delete(request, id=id):

	instance= get_object_or_404(NumObject, id=id)
	if request.user.username == instance.usersave:
		instance.delete()

	else:
		raise PermissionDenied()
	return redirect('posts:list')
# Create your views here.
