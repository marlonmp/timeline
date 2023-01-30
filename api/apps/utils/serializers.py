from rest_framework import serializers

from apps.user import models as um
from apps.project import models as pm
from apps.schedule import models as sm


class ProjectDetail(serializers.ModelSerializer):

    detail = serializers.HyperlinkedIdentityField(view_name='project', lookup_field='uuid')

    class Meta:

        model = pm.Project

        fields = ('uuid', 'title', 'name', 'detail', 'status')


class UserDetail(serializers.ModelSerializer):

    detail = serializers.HyperlinkedIdentityField(view_name='user', lookup_field='uuid')

    class Meta:

        model = um.User

        fields = ('uuid', 'username', 'nickname', 'detail')


class ScheduleTypeDetail(serializers.ModelSerializer):

    detail = serializers.HyperlinkedIdentityField(view_name='schedule-type', lookup_field='uuid')

    class Meta:

        model = sm.ScheduleType

        fields = ('uuid', 'name', 'description', 'detail')


class ScheduleDetail(serializers.ModelSerializer):

    detail = serializers.HyperlinkedIdentityField(view_name='schedule', lookup_field='uuid')

    class Meta:

        model = sm.Schedule

        fields = ('uuid', 'description', 'detail', 'status')


class TaskDetail(serializers.ModelSerializer):

    detail = serializers.HyperlinkedIdentityField(view_name='task', lookup_field='uuid')

    class Meta:

        model = sm.Task

        fields = ('uuid', 'description', 'const_time', 'detail', 'status')

