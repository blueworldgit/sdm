# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    # The home page
    path('', views.index, name='home'),

    # Matches any html file but excludes paths that start with 'attendance'
    re_path(r'^(?!attendance).*$', views.pages, name='pages'),
]
