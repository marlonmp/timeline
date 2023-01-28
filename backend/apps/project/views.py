from rest_framework import generics

from apps.project import serializers as s, models as m


class ProjectListCreate(generics.ListCreateAPIView):

    queryset = m.Project.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        match self.request.method:
            case 'GET':
                return s.ProjectCreate
            case 'POST':
                return s.ProjectList
        return None


class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = m.Project.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        match self.request.method:
            case 'GET':
                return s.ProjectRetrieve
            case 'PUT' | 'PATCH':
                return s.ProjectUpdate
        return None
