from django.conf.urls import url 

urlpatterns = [
	url('/', views.Landing, name='um_landing'),
	url('/user/create', views.Register, name="um_register"),
	url('/user/login', views.Login, name="um_register")
]