from django.urls import path
from . import views

urlpatterns = [
		path('',views.login),
		path('home/',views.Is_logged_in),
		path('registration/',views.registration),
]