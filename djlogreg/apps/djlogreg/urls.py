from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.landing, name="djlogreg-landing"),
	url(r'^register/', views.register, name="djlogreg-register"),
	url(r'^login/', views.login, name="djlogreg-login"),
	url(r'^success/', views.success, name="djlogreg-success"),
	url(r'^logout/', views.logout, name="djlogreg-logout")
]