from django.urls import path
# from apiview.views import StudentList,StudentCreate,StudentRetreive,StudentUpdate,StudentDestroy
from apiview.views import ListCreateStudenAPI,StudentRetriveUpdateDestroyAPI
urlpatterns = [
    # path('',StudentList.as_view()),
    # # here only one url will works for executing genericapiview subclass
    # path('',StudentCreate.as_view()),
    # path('<int:pk>',StudentRetreive.as_view()),
    # path('<int:pk>',StudentUpdate.as_view()),
    # path('<int:pk>',StudentDestroy.as_view())
    path('',ListCreateStudenAPI.as_view()),
    path('<int:pk>',StudentRetriveUpdateDestroyAPI.as_view())
]
