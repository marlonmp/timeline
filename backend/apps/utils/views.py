from rest_framework import generics

from apps.user import models as um
from apps.project import models as pm
from apps.schedule import models as sm

from apps.user import views as uv
from apps.project import views as pv
from apps.schedule import views as sv


class UserProjectsList(pv.ProjectListCreate):

    queryset = um.User.objects.all()
    lookup_field = 'uuid'

    def get_queryset(self):
        user = self.get_object()
        return user.projects

    def post(self, *args, **kwargs):
        self.http_method_not_allowed()


class UserSchedulesList(sv.ScheduleListCreate):

    queryset = um.User.objects.all()
    lookup_field = 'uuid'

    def get_queryset(self):
        user = self.get_object()
        return user.schedules

    def post(self, *args, **kwargs):
        self.http_method_not_allowed()


class UserTasksList(sv.TaskListCreate):

    queryset = um.User.objects.all()
    lookup_field = 'uuid'

    def get_queryset(self):
        user = self.get_object()
        return user.tasks

    def post(self, *args, **kwargs):
        self.http_method_not_allowed()


class ProjectMembersList(uv.UserListCreate):

    queryset = pm.Project.objects.all()
    lookup_field = 'uuid'

    def get_queryset(self):
        project = self.get_object()
        return project.members

    def post(self, *args, **kwargs):
        self.http_method_not_allowed()


class ProjectSchedulesListCreate(sv.ScheduleListCreate):

    queryset = pm.Project.objects.all()
    lookup_field = 'uuid'

    def get_queryset(self):
        project = self.get_object()
        return project.schedules

    def post(self, request, uuid, *args, **kwargs):
        request.data['project'] = uuid
        return super().post(request, *args, **kwargs)


class ScheduleTasksList(sv.TaskListCreate):

    queryset = sm.Schedule.objects.all()
    lookup_field = 'uuid'

    def get_queryset(self):
        schedule = self.get_object()
        return schedule.tasks

    def post(self, *args, **kwargs):
        self.http_method_not_allowed()
