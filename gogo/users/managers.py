from django.db import models
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import exceptions
from django.contrib.auth.hashers import make_password
import datetime

class GoGoManager(models.Manager):
    """
    GoGo User Manager.
    """
    def get_queryset(self):
        return MdlSurveyQuestionCategoryQuerySet(self.model, using=self._db)

    def get_record_by_id(self, id_val):
        return self.get_queryset().get_record_by_id(id_val)

    def get_record_by_user_name(self,username):
        return self.get_queryset().get_record_by_user_name(username)

    def get_username_by_phone_number(self,phone_number):
        return self.get_queryset().get_username_by_phone_number(phone_number)

    def create_record(self, **kwargs):

        user_data = kwargs['user']
        first_name =user_data['first_name']
        last_name = user_data['last_name']
        username = user_data['username']
        password = make_password(user_data['password'])
        phone_number = user_data['phone_number']
        email = user_data['email']
        gender = user_data['gender']

        model_gogo_user = apps.get_model(app_label='users', model_name='GoGoUser')
        user_obj = model_gogo_user(first_name=first_name, last_name=last_name, username=username, password=password,
                                   phone_number=phone_number, email=email,gender=gender,is_self_register=True)
        user_obj.save()
        return user_obj

class MdlSurveyQuestionCategoryQuerySet(models.QuerySet):
    """
    GoGo User QuerySet.
    """

    def get_record_by_id(self, id_val):
        try:
            return self.get(
                id=id_val)
        except ObjectDoesNotExist:
            return None

    def get_record_by_user_name(self,username):
        try:
            return self.get(username=username)
        except ObjectDoesNotExist:
            return None

    def get_username_by_phone_number(self,phone_number):
        try:
            return self.filter(phone_number=phone_number).values_list('username',flat=True)[0]
        except ObjectDoesNotExist:
            return None