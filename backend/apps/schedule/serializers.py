from rest_framework import serializers

from apps.schedule import models as m

from apps.utils import serializers as us


class ScheduleTypeList(serializers.ModelSerializer):

    class Meta:

        model = m.ScheduleType

        fields = ('uuid', 'name', 'description', 'created_at', 'updated_at')


class ScheduleTypeCreate(serializers.ModelSerializer):

    class Meta:

        model = m.ScheduleType

        fields = ('name', 'description')


class ScheduleTypeRetrieve(serializers.ModelSerializer):

    class Meta:

        model = m.ScheduleType

        fields = ('uuid', 'name', 'description')


class ScheduleTypeUpdate(ScheduleTypeCreate):

    pass


# schedule


class ScheduleList(serializers.ModelSerializer):

    project = us.ProjectDetail()

    owner = us.UserDetail()

    type = ScheduleTypeRetrieve()

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


# tasks


class TaskList(serializers.ModelSerializer):

    schedule = us.ScheduleDetail()

    owner = us.UserDetail()

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

# activities

class TaskActionList(serializers.ModelSerializer):

    owner = us.UserDetail()

    dispatcher = us.UserDetail()

    task = us.TaskDetail()

    class Meta:

        model = m.TaskAction

        fields = ('uuid', 'owner', 'dispatcher', 'task', 'description', 'const_time', 'status', 'created_at')
