from django.urls import path
from core.views import home, staff


urlpatterns = [
    path('index/', home),
    path('staff/', staff)
]
