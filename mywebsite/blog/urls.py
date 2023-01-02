from django.urls import path

from .views import blogviews

app_name = 'blog'
urlpatterns = [
    path('list/', blogviews, name='blogList')
]