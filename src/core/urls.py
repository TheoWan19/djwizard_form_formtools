from django.urls import path
from . import views

urlpatterns=[
	path('', views.BookingWizardView.as_view()),
	]