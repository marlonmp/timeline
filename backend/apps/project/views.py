from rest_framework import generics

from apps.project import serializers as s, models as m


class ProjectListCreateAPIView(generics.ListCreateAPIView):

    queryset = m.Project.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        match self.request.method:
            case 'POST':
                return s.ProjectList
            case 'GET':
                return s.ProjectCreate
        return None


class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = m.Project.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        match self.request.method:
            case 'PATCH' | 'PUT':
                return s.ProjectUpdate
            case 'GET':
                return s.ProjectList
        return None

    def perform_destroy(self, instance):
        # if has relations, only change status
        # else, delete
        return super().perform_destroy(instance)
