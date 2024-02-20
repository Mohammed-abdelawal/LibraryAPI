
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


v1_urls = [
    path('book-app/', include("book.urls")),
    path('library-app/', include("library.urls")),

]


urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        'api/v1/',
        include(v1_urls)
    ),
    path(
        'api/token/',
        obtain_auth_token,
        name='obtain-token'
    ),
]
