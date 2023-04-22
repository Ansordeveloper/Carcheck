from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin,UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import filters
from  apps.users.models import User
from apps.users.serializers import UserSerializer,UserRegisterSerializer
from apps.users.permissions import UsersPermissions

class UserAPIViewSet(GenericViewSet,
                     ListModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin,
                     CreateModelMixin,
                     DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('username' , 'email', 'phone_number', 'age')

    def get_serializer_class(self):
        if self.action in ('create',):
            return UserRegisterSerializer
        return UserSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (IsAuthenticated(), UsersPermissions(),)
        return (AllowAny(),)