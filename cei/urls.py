from django.urls import include, path
from rest_framework import routers

from cei.entity import views

router = routers.DefaultRouter()
router.register(r"entities", views.EntityViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
