from django.urls import path
from .views import RegisterView, LoginView, doctor_dashboard, patient_dashboard, LoginView
from .views import custom_logout

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('logout/', custom_logout, name='logout'),
]
