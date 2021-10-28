from django.urls import path
from . import views 


urlpatterns = [
	path('', views.index, name='Homepage'),
	path('Menu1/', views.Menu1, name='Menu1'),
	path('Register/', views.Register, name='Register')

]