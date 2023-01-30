from rest_framework import serializers

from apps.user import models as um
from apps.project import models as m

from apps.utils import serializers as us


class ProjectList(serializers.ModelSerializer):

    class Meta:

        model = m.Project

        fields = ('uuid', 'title', 'name', 'description', 'status')


class ProjectCreate(serializers.ModelSerializer):

    members = serializers.SlugRelatedField(slug_field='uuid', queryset=um.User.objects.all(), many=True)

    class Meta:

        model = m.Project

        fields = ('title', 'name', 'description', 'members')


class ProjectRetrieve(serializers.ModelSerializer):

    members = us.UserDetail(many=True)

    class Meta:

        model = m.Project

        fields = ('title', 'name', 'description', 'members', 'status',  'created_at')


class ProjectUpdate(serializers.ModelSerializer):

    members = serializers.SlugRelatedField(slug_field='uuid', queryset=um.User.objects.all(), many=True)

    class Meta:

        model = m.Project

        fields = ('title', 'name', 'description', 'members', 'status')
