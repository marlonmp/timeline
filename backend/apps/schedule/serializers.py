from rest_framework import serializers

from apps.schedule import models as m

from apps.utils import serializers as us


class ScheduleTypeList(serializers.ModelSerializer):

    class Meta:

        model = m.ScheduleType

        fields = ('uuid', 'name', 'description')


class ScheduleTypeCreate(serializers.ModelSerializer):

    class Meta:

        model = m.ScheduleType

        fields = ('name', 'description')


class ScheduleTypeRetrieve(serializers.ModelSerializer):

    class Meta:

        model = m.ScheduleType

        fields = ('name', 'description', 'created_at', 'updated_at')


class ScheduleTypeUpdate(ScheduleTypeCreate):

    pass


# schedule


class ScheduleList(serializers.ModelSerializer):

    project = us.ProjectDetail()

    owner = us.UserDetail()

    type = us.ScheduleTypeDetail()

    class Meta:

        model = m.Schedule

        fields = ('uuid', 'project', 'owner', 'type', 'description', 'status')


class ScheduleCreate(serializers.ModelSerializer):

    class Meta:

        model = m.Schedule

        fields = ('project', 'owner', 'type', 'description')


class ScheduleRetrieve(serializers.ModelSerializer):

    project = us.ProjectDetail()

    owner = us.UserDetail()

    type = us.ScheduleTypeDetail()

    class Meta:

        model = m.Schedule

        fields = ('project', 'owner', 'type', 'description', 'status', 'created_at')


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

        fields = ('uuid', 'schedule', 'owner', 'description', 'const_time', 'status')


class TaskCreate(serializers.ModelSerializer):

    class Meta:

        model = m.Task

        fields = ('schedule', 'owner', 'description', 'const_time')


class TaskRetrieve(serializers.ModelSerializer):

    schedule = us.ScheduleDetail()

    owner = us.UserDetail()

    class Meta:

        model = m.Task

        fields = ('schedule', 'owner', 'description', 'const_time', 'status', 'created_at')


class TaskUpdate(serializers.ModelSerializer):

    class Meta:

        model = m.Task

        fields = ('schedule', 'owner', 'description', 'const_time', 'status')
