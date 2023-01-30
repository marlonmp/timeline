from apps.utils import mixins

from apps.user import models as um
from apps.project import models as pm
from apps.schedule import models as sm

from apps.user import views as uv
from apps.project import views as pv
from apps.schedule import views as sv


class UserProjectsList(mixins.ListFieldViewMixin, pv.ProjectListCreate):

    queryset = um.User.objects.all()
    lookup_field = 'uuid'
    list_field = 'projects'

    def post(self, *args, **kwargs):
        self.http_method_not_allowed()


class UserSchedulesList(mixins.ListFieldViewMixin, sv.ScheduleListCreate):

    queryset = um.User.objects.all()
    lookup_field = 'uuid'
    list_field = 'schedules'

    def post(self, *args, **kwargs):
        self.http_method_not_allowed()


class UserTasksList(mixins.ListFieldViewMixin, sv.TaskListCreate):

    queryset = um.User.objects.all()
    lookup_field = 'uuid'
    list_field = 'tasks'

    def post(self, *args, **kwargs):
        self.http_method_not_allowed()


class ProjectMembersList(mixins.ListFieldViewMixin, uv.UserListCreate):

    queryset = pm.Project.objects.all()
    lookup_field = 'uuid'
    list_field = 'members'

    def post(self, *args, **kwargs):
        self.http_method_not_allowed()


class ProjectSchedulesListCreate(mixins.ListFieldViewMixin, sv.ScheduleListCreate):

    queryset = pm.Project.objects.all()
    lookup_field = 'uuid'
    list_field = 'schedules'

    def post(self, request, uuid, *args, **kwargs):
        request.data['project'] = uuid
        return super().post(request, *args, **kwargs)


class ScheduleTasksList(mixins.ListFieldViewMixin, sv.TaskListCreate):

    queryset = sm.Schedule.objects.all()
    lookup_field = 'uuid'
    list_field = 'tasks'

    def post(self, *args, **kwargs):
        self.http_method_not_allowed()
