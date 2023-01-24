from rest_framework import serializers

from apps.project import models as m


class ProjectList(serializers.ModelSerializer):

    class Meta:

        model = m.Project

        fields = ('uuid', 'title', 'name', 'description', 'members', 'status', 'created_at')


class ProjectCreate(serializers.ModelSerializer):

    class Meta:

        model = m.Project

        fields = ('title', 'name', 'description', 'members')


class ProjectUpdate(serializers.ModelSerializer):

    class Meta:

        model = m.Project

        fields = ('title', 'name', 'description', 'members', 'status')


class ScheduleTypeList(serializers.ModelSerializer):

    class Meta:

        model = m.ScheduleType

        fields = ('uuid', 'name', 'description', 'created_at', 'updated_at')


class ScheduleTypeCreate(serializers.ModelSerializer):

    class Meta:

        model = m.ScheduleType

        fields = ('name', 'description')


class ScheduleTypeUpdate(ScheduleTypeCreate):

    pass


class ScheduleList(serializers.ModelSerializer):

    class Meta:

        model = m.Schedule

        fields = ('uuid', 'project', 'owner', 'type', 'description', 'status', 'created_at')


class ScheduleCreate(serializers.ModelSerializer):

    class Meta:

        model = m.Schedule

        fields = ('project', 'owner', 'type', 'description')


class ScheduleUpdate(serializers.ModelSerializer):

    class Meta:

        model = m.Schedule

        fields = ('project', 'owner', 'type', 'description', 'status')


class TaskList(serializers.ModelSerializer):

    class Meta:

        model = m.Task

        fields = ('uuid', 'schedule', 'owner', 'description', 'const_time', 'status', 'created_at')


class TaskCreate(serializers.ModelSerializer):

    class Meta:

        model = m.Task

        fields = ('schedule', 'owner', 'description', 'const_time')


class TaskUpdate(serializers.ModelSerializer):

    class Meta:

        model = m.Task

        fields = ('schedule', 'owner', 'description', 'const_time', 'status')
