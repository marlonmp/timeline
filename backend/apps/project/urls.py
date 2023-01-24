from rest_framework.routers import DefaultRouter

from apps.project import views as v

router = DefaultRouter()

router.register(r'projects', v.ProjectViewSet, basename='projects')
router.register(r'schedule-types', v.ScheduleTypeViewSet, basename='schedule-types')
router.register(r'schedules', v.ScheduleViewSet, basename='schedules')
router.register(r'tasks', v.TaskViewSet, basename='tasks')

urlpatterns = router.urls
