from django.urls import path
from rest_framework import routers
from django.conf.urls import url, include

from users.api.views import users_views


class GoGoUsersAPI(routers.APIRootView):
    pass


class DocumentedRouter(routers.DefaultRouter):
    APIRootView = GoGoUsersAPI


router = DocumentedRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('register/', users_views.GogoUserRegisterView.as_view()),
    path('login/', users_views.GogoLoginView.as_view()),
]
