from django import forms
from .models import Application

class ApproveHall1Form(forms.ModelForm):
	approve = forms.CharField()

	class Meta:
		model = Application
		fields = ['approve']

class ApproveHall2Form(forms.ModelForm):
	approve = forms.CharField()

	class Meta:
		model = Application
		fields = ['approve']

class ApproveHall3Form(forms.ModelForm):
	approve = forms.CharField()

	class Meta:
		model = Application
		fields = ['approve']