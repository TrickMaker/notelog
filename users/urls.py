"""Defines url patterns for users."""

from django.urls import include,path,re_path
from django.contrib.auth.views import login

from . import views
app_name = 'users'
urlpatterns = [
    # Login page.
    re_path(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),

    # Logout page.
    re_path(r'^logout/$', views.logout_view, name='logout'),

    # Registration page.
    re_path(r'^register/$', views.register, name='register'),
]