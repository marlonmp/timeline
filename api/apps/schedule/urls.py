from rest_framework.urls import path

from apps.schedule import views as v
from apps.utils import views as uv

urlpatterns = [
    path('schedule-types', v.ScheduleTypeListCreate.as_view(), name='schedule-types'),
    path('schedule-types/<uuid:uuid>', v.ScheduleTypeRetrieveUpdateDestroy.as_view(), name='schedule-type'),

    path('schedules', v.ScheduleListCreate.as_view(), name='schedules'),
    path('schedules/<uuid:uuid>', v.ScheduleRetrieveUpdateDestroy.as_view(), name='schedule'),

    path('schedules/<uuid:uuid>/tasks', uv.ScheduleTasksList.as_view(), name='schedule-tasks'),

    path('tasks', v.TaskListCreate.as_view(), name='tasks'),
    path('tasks/<uuid:uuid>', v.TaskRetrieveUpdateDestroy.as_view(), name='task'),
]
