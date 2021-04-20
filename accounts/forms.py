from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.db import transaction
from .models import User, Student, Admin, Profile

class StudentRegisterForm(UserCreationForm):
	username = UsernameField(
		max_length=7,
		min_length=7,
        label='Student ID',
        widget=forms.TextInput(attrs={'autofocus': True}),
        required=True
    )
	name = forms.CharField(required=True)
	password1 = forms.CharField(
		label="Password",
		widget=forms.PasswordInput(attrs={'class':'form-input', 'type':'password'}))
	password2 = forms.CharField(
		label="Confirm password",
		widget=forms.PasswordInput(attrs={'class':'form-input', 'type':'password'}))


	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['name', 'email', 'username', 'password1', 'password2']
		widgets={'email':forms.TextInput(attrs={'class':'form-input', 'type':'text'})}

class AdminRegisterForm(UserCreationForm):
	username = UsernameField(
        label='Name',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
	designation = forms.CharField(max_length=50, required=True)
	password1 = forms.CharField(
		label="Password",
		widget=forms.PasswordInput(attrs={'class':'form-input', 'type':'password'}))
	password2 = forms.CharField(
		label="Confirm password",
		widget=forms.PasswordInput(attrs={'class':'form-input', 'type':'password'}))

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['username', 'email', 'designation', 'password1', 'password2']
		widgets={'email':forms.TextInput(attrs={'class':'form-input', 'type':'text'})}

class StudentLoginForm(AuthenticationForm):
	username = UsernameField(
		max_length=7,
		min_length=7,
		label='Student ID',
		widget=forms.TextInput(attrs={'autofocus': True}),
		required=True
	)
	password = forms.CharField(
		label="Password",
		widget=forms.PasswordInput(attrs={'class':'form-input', 'type':'password'}))

class AdminLoginForm(AuthenticationForm):
	username = UsernameField(
		label='Name',
		widget=forms.TextInput(attrs={'autofocus': True}),
		required=True
	)
	password = forms.CharField(
		label="Password",
		widget=forms.PasswordInput(attrs={'class':'form-input', 'type':'password'}))

class UserUpdateForm(forms.ModelForm):
	username = UsernameField(
		max_length=7,
		min_length=7,
		label='Student ID',
		widget=forms.TextInput(attrs={'autofocus': True}),
		required=True
	)
	class Meta:
		model = User
		fields = ['username', 'email']
		widgets={'email':forms.TextInput(attrs={'class':'form-input', 'type':'text'})}

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']