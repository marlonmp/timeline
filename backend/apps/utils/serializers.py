from rest_framework import serializers

from apps.user import models as um
from apps.project import models as pm
from apps.schedule import models as sm


class ProjectDetail(serializers.ModelSerializer):

    detail = serializers.HyperlinkedIdentityField(view_name='project-detail')

    class Meta:

        model = pm.Project

        fields = ('uuid', 'title', 'name', 'detail', 'status')


class UserDetail(serializers.ModelSerializer):

    # add user retrieve view name
    detail = serializers.HyperlinkedIdentityField(view_name='user-detail')

    class Meta:

        model = um.User

        fields = ('uuid', 'username', 'nickname', 'detail')


class ScheduleDetail(serializers.ModelSerializer):

    detail = serializers.HyperlinkedIdentityField(view_name='schedule-detail')

    class Meta:

        model = sm.Schedule

        fields = ('uuid', 'description', 'detail', 'status')


class TaskDetail(serializers.ModelSerializer):

    detail = serializers.HyperlinkedIdentityField(view_name='task-detail')

    class Meta:

        model = sm.Task

        fields = ('uuid', 'description', 'const_time', 'detail', 'status')


class TaskActionDetail(serializers.ModelSerializer):

    detail = serializers.HyperlinkedIdentityField(view_name='task-action-detail')

    class Meta:

        model = sm.TaskAction

        fields = ('uuid', 'description', 'const_time', 'detail', 'status')
