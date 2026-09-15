from django.urls import path
from blog.views import blog_list



urlpatterns = [
    path('blogs/', blog_list)
]
