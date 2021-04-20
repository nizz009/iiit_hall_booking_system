from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import User, Student, Admin
from halls.models import Application
from .forms import StudentRegisterForm, AdminRegisterForm, StudentLoginForm, AdminLoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def student_register(request):
	if request.method == 'POST':
		form = StudentRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			student = Student.objects.create(user=user)
			student.name = form.cleaned_data.get('name')
			student.save()
			messages.success(request, f'Your account was created successfully. You can now log in.')
			return redirect('acc-student-login')
	else:
		form = StudentRegisterForm()
	return render(request, 'accounts/student_register.html', {'form': form, 'title': 'Registration'})

def admin_register(request):
	if request.method == 'POST':
		form = AdminRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			user.is_admin = "True"
			email = form.cleaned_data.get('email')
			admin = Admin.objects.create(user=user)
			admin.designation = form.cleaned_data.get('designation')
			admin.save()
			messages.success(request, f'Your account was created successfully. You can now log in.')
			return redirect('acc-admin-login')
	else:
		form = AdminRegisterForm()
	return render(request, 'accounts/admin_register.html', {'form': form, 'title': 'Registration'})


def student_login(request):
	if request.method == 'POST':
		form = StudentLoginForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('halls-home')
	else:
		form = StudentLoginForm()
	return render(request, 'accounts/student_login.html', {'form': form, 'title': 'Student Login'})


def admin_login(request):
	if request.method == 'POST':
		form = AdminLoginForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('halls-home')
	else:
		form = AdminLoginForm()
	return render(request, 'accounts/admin_login.html', {'form': form, 'title': 'Admin Login'})


def logout_view(request):
	logout(request)
	messages.success(request, f'You have succesfully logged out.')
	return redirect('halls-home')

@login_required
def profile(request):
	context = {
		'applications': Application.objects.all()
	}
	return render(request, 'accounts/profile.html', context)

@login_required
def profile_update(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated successfully.')
			return redirect('acc-profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form,
		'title': 'Update Profile'
	}

	return render(request, 'accounts/profile_update.html', context)