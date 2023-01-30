from rest_framework import generics

from apps.user import serializers as s, models as m


class UserListCreate(generics.ListCreateAPIView):

    queryset = m.User.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        match self.request.method:
            case 'GET':
                return s.UserList
            case 'POST':
                return s.UserCreate
        return None


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = m.User.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        match self.request.method:
            case 'GET':
                return s.UserRetrieve
            case 'PUT' | 'PATCH':
                return s.UserUpdate
        return None
