from django.urls import path
from apiview.views import *
urlpatterns = [
    # here at a time only view class executed
    # path('',StudentList.as_view()),
    # path('',StudentCreate.as_view()),
    # path('<int:pk>',StudentRetrieve.as_view()),
    # path('<int:pk>',StudentDestroy.as_view()),
    # path('<int:pk>',StudentUpdate.as_view())
    ############################################################
    # path('',StudentListCreateAPIView.as_view()),
    # path('<int:pk>',StudentRetrieveUpdateAPIView.as_view()),
    # path('<int:pk>',StudentRetrieveDestroyAPIView.as_view()),
    # path('<int:pk>',StudentRetrieveUpdateDestroyAPIView.as_view())
    ####################################################################
    path('',StudentListCreateAPIView.as_view()),
    path('<int:pk>',StudentRetrieveUpdateDestroyAPIView.as_view())
]
