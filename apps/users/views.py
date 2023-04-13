from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin,UpdateModelMixin

from  apps.users.models import User
from apps.users.serializers import UserSerializer,UserRegisterSerializer

class UserAPIViewSet(GenericViewSet,
                     ListModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin,
                     CreateModelMixin,
                     DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action in ('create',):
            return UserRegisterSerializer
        return UserSerializer