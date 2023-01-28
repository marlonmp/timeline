from rest_framework.urls import path

from apps.project import views as v
from apps.utils import views as uv

urlpatterns = [
    path('projects', v.ProjectListCreate.as_view(), name='projects'),
    path('projects/<uuid:uuid>', v.ProjectRetrieveUpdateDestroy.as_view(), name='project'),

    path('projects/<uuid:uuid>/members', uv.ProjectMembersList.as_view(), name='project-members'),

    path('projects/<uuid:uuid>/schedules', uv.ProjectSchedulesListCreate.as_view(), name='project-schedules'),
]
