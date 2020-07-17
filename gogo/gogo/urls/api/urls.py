from django.conf.urls import include, url
from django.urls import path


urlpatterns = [
    # apps urls
    url(r'^users/', include('users.api.urls.users_urls')),
]