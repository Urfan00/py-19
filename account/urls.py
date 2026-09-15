from django.urls import path
from account.views import user_list


urlpatterns = [
    path('users/', user_list)
]
