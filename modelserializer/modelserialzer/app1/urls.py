from django.urls import path
from app1.views import StudentApi
urlpatterns = [
    path('',StudentApi.as_view())
]
