from rest_framework import serializers


class UserCredentials(serializers.Serializer):

    username = serializers.CharField(max_length=150)

    password = serializers.CharField(max_length=128)
