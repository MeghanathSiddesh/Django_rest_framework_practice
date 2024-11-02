from apiview.models import Student
from apiview.serializers import StudentSerializer
# from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
'''class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentRetrieve(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentDestroy(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer'''
# while using concrete ai class the problem is while defining url we need to define them for each http method so most people dont prefer them and if we create same url for all http methods perform view function one view will override other
'''class StudentListCreateAPIView(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer'''

##############################################################################
# insted of using all we can use two classes that will do all work
class StudentListCreateAPIView(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer