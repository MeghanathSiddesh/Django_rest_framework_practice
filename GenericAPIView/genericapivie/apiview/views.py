# GenericAPIView and Model Mixin
from apiview.models import Student
from apiview.serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

'''class StudentList(GenericAPIView,ListModelMixin):
    # here queryset and serializer_class attributes are by predefined attributes
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # get function specifies that it accepts get requests
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class StudentRetreive(GenericAPIView,RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # here we have two options either retreive entire data or retreive specific data to retreive entire data use ListModelMixin but for an instance use RetriveModelMixix
    # so to retreive a specific data here get method is expecting some id value from the requesting app so it is neseccary to use <int:pk> in the url path in urlpatterns
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
class StudentCreateList(GenericAPIView,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class StudentDestroy(GenericAPIView,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)'''
class ListCreateStudenAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    # List and Create -PK Not required
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
# Retreive Update and Destroy
class StudentRetriveUpdateDestroyAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)