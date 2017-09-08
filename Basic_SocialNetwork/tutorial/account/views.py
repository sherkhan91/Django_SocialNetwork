# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from account.forms import RegistrationForm, EditProfileForm 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
"""
def home(request):
	numbers = [1,2,3,4,5]
	name = "Max Goodridge"
	args = {'myName': name, 'numbers': numbers}
	return render(request, 'account/home.html', args)
"""

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account/login/')


	else:
		form = RegistrationForm()
		args = {'form': form}
		return render(request, 'account/reg_form.html', args)
		#return render(request, '{% url "" ' %}', args)		


def view_profile(request, pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user = request.user	
	args = {'user': user}
	return render(request, 'account/profile.html', args)	



def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/account/profile')
			#return redirect(url =view_profile)
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form': form }
		return render(request, 'account/edit_profile.html', args)	
	
	
def change_password(request):
	if request.method=='POST':
		form = PasswordChangeForm(data = request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/account/profile')
		else:
			return redirect('/account/change-password')	
	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form': form}
		return render(request, 'account/change_password.html', args)		