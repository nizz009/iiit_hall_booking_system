from django.urls import path
from .views import (
	ApplicationListView, 
	ApplicationDetailView,
	ApplicationCreateView,
	ApplicationUpdateView, 
	ApplicationDeleteView
)
from . import views

urlpatterns = [
    path('', views.home, name='halls-home'),
    path('halls/', views.halls_list, name='halls-list'),
    path('halls/hall1/', views.hall_1, name='hall-1'),
    path('halls/hall2/', views.hall_2, name='hall-2'),
    path('halls/hall3/', views.hall_3, name='hall-3'),
    path('applications/', ApplicationListView.as_view(), name='all-applications'),
    path('applications/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('applications/new/', ApplicationCreateView.as_view(), name='application-create'),
    path('applications/<int:pk>/update/', ApplicationUpdateView.as_view(), name='application-update'),
    path('applications/<int:pk>/delete/', ApplicationDeleteView.as_view(), name='application-delete'),
    path('applications/<int:pk>/approve1/', views.approve_hall1, name='application-approve1'),
    path('applications/<int:pk>/approve2/', views.approve_hall2, name='application-approve2'),
    path('applications/<int:pk>/approve3/', views.approve_hall3, name='application-approve3'),
]
