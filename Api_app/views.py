from rest_framework import viewsets, mixins
from .models import User, Trash, Ramassage
from .serializers import UserSerializer, TrashSerializer, RamassageSerializer,EnterpriseSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from Api_app.models import User
from .serializers import UserSerializer
from .permissions import IsEnterprise
from rest_framework import permissions


class EnterpriseViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated, IsEnterprise]
    queryset = User.objects.filter(is_enterprise=True)
    serializer_class = EnterpriseSerializer

    
class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        user_data = request.data
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = User.objects.create_user(
                username=user_serializer.validated_data['username'],
                email=user_serializer.validated_data['email'],
                password=user_serializer.validated_data['password']
            )
            user.save()
            user_profile = User(user=user, is_enterprise=user_data.get('is_enterprise', False))
            user_profile.save()
            return Response({"status": "success", "data": UserSerializer(user_profile).data})
        else:
            return Response({"status": "error", "data": user_serializer.errors})

class TrashViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Trash.objects.all()
    serializer_class = TrashSerializer

class RamassageViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Ramassage.objects.all()
    serializer_class = RamassageSerializer

