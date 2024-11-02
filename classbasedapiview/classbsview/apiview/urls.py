from django.urls import path
from apiview.views import StudentApi
urlpatterns = [
    path('<int:pk>',StudentApi.as_view()),
    path('',StudentApi.as_view())
]
