from django.urls import path
from . import views

app_name = 'api'


urlpatterns = [
    path('', views.index, name="homepage"),

    path('country/', views.country, name='country'),
    path('state/', views.state, name="state"),
    path('city/', views.city, name='city')
]