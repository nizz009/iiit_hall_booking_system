from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Hall_1, Hall_2, Hall_3, Application
from accounts.models import User
from .forms import ApproveHall1Form, ApproveHall2Form, ApproveHall3Form
from django.contrib import messages


# Create your views here.

def home(request):
	return render(request, 'halls/home.html', {'title': 'Home'})

def halls_list(request):
	return render(request, 'halls/halls_list.html', {'title': 'Auditorium Halls'})

def hall_1(request):
	context = { 
		'schedule': Hall_1.objects.all(),
		'title': 'Mini Audi'
	}
	return render(request, 'halls/hall_1.html', context)

def hall_2(request):
	context = { 
		'schedule': Hall_2.objects.all(),
		'title': 'AG-01'
	}
	return render(request, 'halls/hall_2.html', context)

def hall_3(request):
	context = { 
		'schedule': Hall_3.objects.all(),
		'title': 'AG-02'
	}
	return render(request, 'halls/hall_3.html', context)

def all_applications(request):
	context = { 
		'applications': Application.objects.all(),
		'title': 'All Applications'
	}
	return render(request, 'halls/all_applications.html', context)

class ApplicationListView(ListView):
	model = Application
	template_name = 'halls/all_applications.html'
	context_object_name = 'applications'
	ordering = ['-date']

class ApplicationDetailView(DetailView):
	model = Application


class ApplicationForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['hall_name'].widget.attrs.update({'class' : 'form-group form-control'})
		self.fields['name'].widget.attrs.update({'class' : 'form-group form-control'})
		self.fields['purpose'].widget.attrs.update({'class' : 'form-group form-control'})
		self.fields['date'].widget.attrs.update({'class' : 'form-group form-control'})
		self.fields['start_time'].widget.attrs.update({'class' : 'form-group form-control'})
		self.fields['end_time'].widget.attrs.update({'class' : 'form-group form-control'})

	class Meta:
		model = Application
		fields = ['hall_name', 'name', 'purpose', 'date', 'start_time', 'end_time']

class ApplicationCreateView(LoginRequiredMixin, CreateView):
	form_class = ApplicationForm
	model = Application

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class ApplicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Application
	fields = ['name', 'purpose', 'date', 'start_time', 'end_time']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		application = self.get_object()
		if self.request.user == application.author:
			return True
		return False

class ApplicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Application
	success_url = '/hbms'

	def test_func(self):
		application = self.get_object()
		if self.request.user == application.author:
			return True
		return False

class ApplicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Application
	fields = ['name', 'purpose', 'date', 'start_time', 'end_time']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		application = self.get_object()
		if self.request.user == application.author:
			return True
		return False

def approve_hall1(request, pk):
	application = Application.objects.get(id = pk)

	if request.method == 'POST':

		form = ApproveHall3Form(request.POST, instance = application)

		if form.is_valid():
			approve = form.save()
			application.approve = form.cleaned_data.get('approve')
			if application.approve == 'y' or application.approve == 'Y':
				hall_1 = Hall_1.objects.create(
						name = application.name, 
						purpose = application.purpose,
						date = application.date,
						start_time = application.start_time,
						end_time = application.end_time
					)
				hall_1.save()
				messages.success(request, f'The application was accepted.')
			elif application.approve == 'n' or application.approve == 'N':
				messages.error(request, f'The application was not accepted.')
			return redirect('all-applications')
	else:
		form = ApproveHall3Form()
	return render(request, 'halls/application_approve.html', {'form': form, 'title': 'Application Details', 'application': application})



def approve_hall2(request, pk):
	application = Application.objects.get(id = pk)

	if request.method == 'POST':

		form = ApproveHall3Form(request.POST, instance = application)

		if form.is_valid():
			approve = form.save()
			application.approve = form.cleaned_data.get('approve')
			if application.approve == 'y' or application.approve == 'Y':
				hall_2 = Hall_2.objects.create(
						name = application.name, 
						purpose = application.purpose,
						date = application.date,
						start_time = application.start_time,
						end_time = application.end_time
					)
				hall_2.save()
				messages.success(request, f'The application was accepted.')
			elif application.approve == 'n' or application.approve == 'N':
				messages.error(request, f'The application was not accepted.')
			return redirect('all-applications')
	else:
		form = ApproveHall3Form()
	return render(request, 'halls/application_approve.html', {'form': form, 'title': 'Application Details', 'application': application})



def approve_hall3(request, pk):
	application = Application.objects.get(id = pk)

	if request.method == 'POST':

		form = ApproveHall3Form(request.POST, instance = application)

		if form.is_valid():
			approve = form.save()
			application.approve = form.cleaned_data.get('approve')
			if application.approve == 'y' or application.approve == 'Y':
				hall_3 = Hall_3.objects.create(
						name = application.name, 
						purpose = application.purpose,
						date = application.date,
						start_time = application.start_time,
						end_time = application.end_time
					)
				hall_3.save()
				messages.success(request, f'The application was accepted.')
			elif application.approve == 'n' or application.approve == 'N':
				messages.error(request, f'The application was not accepted.')
			return redirect('all-applications')
	else:
		form = ApproveHall3Form()
	return render(request, 'halls/application_approve.html', {'form': form, 'title': 'Application Details', 'application': application})
