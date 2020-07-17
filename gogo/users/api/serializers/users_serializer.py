from django.db import IntegrityError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.serializers import (
    ModelSerializer,
)
from users.models import (
    GoGoUser
)

import logging,bcrypt
from django.contrib.auth.hashers import check_password

# from base_app.utils import get_user_role

logger = logging.getLogger(__name__)


class GoGoUserSerializer(ModelSerializer):

    class Meta:
        model = GoGoUser
        fields =  ['username','first_name','last_name','email','password','phone_number','gender']

    def user_register(self,data):

        try:
            record = GoGoUser.objects.create_record(**data)
            return True, record
        except Exception as err:
            logging.info(err)
            return False,'Unable to register user'

    def authenticate_user(self, username, password):

        try:
            if username.isdigit() is True:
                username = GoGoUser.objects.get_username_by_phone_number(username)
        except:
            return False,'Incorrect phone number'

        try:
            login_user = GoGoUser.objects.get_record_by_user_name(username)
            if login_user is not None:
                if check_password(password, login_user.password) is True:
                    refresh = RefreshToken.for_user(login_user)
                    logger.info("login_user.id : " + str(login_user.id))

                    user_details = {
                        'first_name': login_user.first_name,
                        'last_name': login_user.last_name,
                        'email': login_user.email,
                        'username': login_user.username,
                        'phone_number':login_user.phone_number
                    }
                    return True, {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'user_details': user_details
                    }
                else:
                    return False, {
                        "error": "Invalid password"
                    }
            else:
                return False, {
                    "error": "User not found"
                }

        except IntegrityError as err:
            logger.error(str(err))
            return False, {
                "error": "Unable to login"
            }