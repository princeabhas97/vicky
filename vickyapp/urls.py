from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from vickyapp import views

urlpatterns = [
path('viewer/', views.vicky_views),
path('getter/', views.get_views2),
]

urlpatterns = format_suffix_patterns(urlpatterns)