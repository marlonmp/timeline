from rest_framework import serializers

from apps.user import models as m


class UserList(serializers.ModelSerializer):

    class Meta:

        model = m.User

        fields = ('uuid', 'username', 'nickname', 'email', 'status')


class UserCreate(serializers.ModelSerializer):

    class Meta:

        model = m.User

        fields = ('username', 'nickname', 'email', 'password')


class UserRetrieve(serializers.ModelSerializer):

    class Meta:

        model = m.User

        fields = ('uuid', 'username', 'nickname', 'email', 'status', 'created_at')


class UserUpdate(serializers.ModelSerializer):

    class Meta:

        model = m.User

        fields = ('username', 'nickname', 'status')
