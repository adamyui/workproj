# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .models import NumObject, Sounds, BlackList
from .forms import PostForm, NumForm, BlacklistForm, AddRules
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin
import json



#main wall displaying all your numbers
def index(request):
	
	listboy= NumObject.objects.all()
	instance= Sounds.objects.all()
	
	context= {
		'object_listboy': listboy,
		'instance':instance,
				
	}
	return render(request, 'wall.html', context)

#Your number detail 
def post_detail(request,id= None):
	instance= get_object_or_404(NumObject, id=id)
	incomingform= BlacklistForm(request.POST or None, request.FILES or None)
	

	if incomingform.is_valid():
		instanceIncoming = incomingform.save(commit=False)
		instanceIncoming.save()
		# return redirect('posts:list')
	
	context= {

		'incomingform': incomingform,
		# 'form' :incomingform,
		'title': instance.number,
		'instance': instance,
		'numkey': instance.title,
		
	}
	return render(request,'post_detail.html',context)


def sound_detail(request, id=None):
	instance= get_object_or_404(NumObject, id=id)
	

	context= {		
		'instance': instance,
	}
	return render(request,'sound_detail.html',context)


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
# def bl_createrules(UpdateView):
# 	model = 
# 	form= AddRules(request.POST or None, request.FILES or None)


# 	if form.is_valid():

# 		instance = form.save(commit=False)
# 		# instance.user = User.objects.get(user=self.request.user)
# 		instance.save()
# 		return HttpResponseRedirect('/')

	
# 	context= {
# 		'form': form,
# 	}
# 	return render(request,'post_detail.html',context)


#DELETE SOUND VIEW
def post_delete(request, id):
	sound= get_object_or_404(Sounds, pk=id).delete()
	
	return redirect('posts:list')


#AJAX MIXIN
class AjaxableResponseMixin(object):
	def render_to_json_response(self, context, **response_kwargs):
		data = json.dumps(context)
		response_kwargs['content_type'] = 'application/json'
		return HttpResponse(data, **response_kwargs)

	def form_invalid(self, form):
		response = super(AjaxableResponseMixin, self).form_invalid(form)
		if self.request.is_ajax():
			return self.render_to_json_response(form.errors, status=400)
		else:
			return response

		def form_valid(self, form):
			response = super(AjaxableResponseMixin, self).form_valid(form)
		if self.request.is_ajax():
			data = {
			'pk': self.object.pk,
			}
			return self.render_to_json_response(data)
		else:
			return response




#UPDATE VIEW
class UpdateRules(AjaxableResponseMixin, UpdateView):
	


	model = BlackList
	form_class = AddRules	
	template_name= 'blacklist_form.html'



	
	


