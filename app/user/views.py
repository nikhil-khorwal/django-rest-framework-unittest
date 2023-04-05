from rest_framework import (generics, authentication, permissions)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import (
    UserSerizlizer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerizlizer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerizlizer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # retrieve and return the authenticated user
    def get_object(self):
        return self.request.user