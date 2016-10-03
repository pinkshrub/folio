from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^', views.landing, name="dm_landing"),
	url(r'^register/', views.register, name="dm_register"),
	url(r'^login/', views.log_in, name="dm_log_in"),
	url(r'^main/', views.main, name="dm_main")
]