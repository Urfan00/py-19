from django.urls import path
from core.views import contact


urlpatterns = [
    path('contact/', contact, name="contact"), 
]

