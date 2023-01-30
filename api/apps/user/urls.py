from rest_framework.urls import path

from apps.user import views as v
from apps.utils import views as uv

urlpatterns = [
    path('users', v.UserListCreate.as_view(), name='users'),
    path('users/<uuid:uuid>', v.UserRetrieveUpdateDestroy.as_view(), name='user'),

    path('users/<uuid:uuid>/projects', uv.UserProjectsList.as_view(), name='user-projects'),

    path('users/<uuid:uuid>/schedules', uv.UserSchedulesList.as_view(), name='user-schedules'),

    path('users/<uuid:uuid>/tasks', uv.UserTasksList.as_view(), name='user-tasks'),
]
