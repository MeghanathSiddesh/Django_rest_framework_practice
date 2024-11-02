from django.urls import path
from apiview.views import Stuent_api
urlpatterns = [
    path('',Stuent_api)
]
