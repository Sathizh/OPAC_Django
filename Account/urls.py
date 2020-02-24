from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

app_name='account'

urlpatterns=[
			path('signup/',views.SignUp.as_view(),name='signup'),
			path('login/',LoginView.as_view(template_name='Account/login.html'),name='login'),
			path('logout',LogoutView.as_view(),name='logout'),
]