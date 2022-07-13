from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from cei.entity import views

router = routers.DefaultRouter()
router.register(r"entities", views.EntityViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
