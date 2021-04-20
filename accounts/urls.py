from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.student_register, name='acc-student-register'),
    path('admin_register/', views.admin_register, name='acc-admin-register'),
    path('student_login/', views.student_login, name='acc-student-login'),
    path('admin_login/', views.admin_login, name='acc-admin-login'),
    path('logout/', views.logout_view, name='acc-logout'),
    path('profile/', views.profile, name='acc-profile'),
    path('profile/update/', views.profile_update, name='acc-profile-update'),
]
