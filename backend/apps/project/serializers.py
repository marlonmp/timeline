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
