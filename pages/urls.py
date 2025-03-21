from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),  # This will map the root URL to the home view
    path('about-us/', views.about_us, name='about_us'),
]
