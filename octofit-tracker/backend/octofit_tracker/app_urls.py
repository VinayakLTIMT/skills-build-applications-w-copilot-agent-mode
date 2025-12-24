from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet, api_root
import os
from rest_framework.response import Response
from rest_framework.decorators import api_view

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboards', LeaderboardViewSet)

@api_view(['GET'])
def custom_api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME', '')
    base_url = request.build_absolute_uri('/')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/"
    return Response({
        'users': f"{base_url}api/users/",
        'teams': f"{base_url}api/teams/",
        'activities': f"{base_url}api/activities/",
        'workouts': f"{base_url}api/workouts/",
        'leaderboards': f"{base_url}api/leaderboards/",
    })

urlpatterns = [
    path('', custom_api_root, name='api-root'),
    path('api/', include(router.urls)),
]
