from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..serializers.users_serializer import GoGoUserSerializer

from rest_framework import (
    generics,
    status,
)
import logging
from base_app.utils import get_request_value
logger = logging.getLogger(__name__)


class GogoLoginView(generics.CreateAPIView):

    def get_serializer_context(self):
        return {'request': self.request}

    def post(self, request, *args, **kwargs):

        user_name = get_request_value(request, 'username', '')
        password = get_request_value(request, 'password', '')

        login_serializer = GoGoUserSerializer()
        result_data = login_serializer.authenticate_user(user_name,password)

        if not result_data[0]:
            return Response(result_data[1], status.HTTP_400_BAD_REQUEST)
        else:
            return Response(result_data[1], status=status.HTTP_200_OK)


class GogoUserRegisterView(generics.CreateAPIView):

    def get_serializer_context(self):
        return {'request': self.request}

    def post(self, request, *args, **kwargs):

        user_register_serializer = GoGoUserSerializer(data=request.data)
        user_register_serializer.is_valid()

        user_register = user_register_serializer.user_register(data=dict(
            user=user_register_serializer.data))

        if not user_register[0]:
            return Response(user_register[1], status.HTTP_400_BAD_REQUEST)
        else:
            user_serializer = GoGoUserSerializer(user_register[1])
            return Response(user_serializer.data, status=status.HTTP_200_OK)