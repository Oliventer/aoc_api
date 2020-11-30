from django.urls import path, include
from rest_framework.routers import DefaultRouter
from problems import views

router = DefaultRouter()
router.register(r'problems', views.ProblemViewset)

urlpatterns = [
    path('', include(router.urls)),
]
