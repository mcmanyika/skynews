from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .views import LibsListView

urlpatterns = [
    url(r'^$', LibsListView.as_view(), name="libs"),
]
