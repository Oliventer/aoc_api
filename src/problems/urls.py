from django.urls import path, include
from rest_framework_nested import routers
from problems import views


router = routers.DefaultRouter()
router.register(r'advents', views.AdventViewset)

problems_router = routers.NestedDefaultRouter(router, r'advents', lookup='advent')
problems_router.register(r'problems', views.ProblemViewset, basename='advent-problems')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(problems_router.urls)),
]
