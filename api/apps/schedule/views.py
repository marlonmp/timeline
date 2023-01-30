from rest_framework import generics

from apps.schedule import models as m, serializers as s

# schedule type


class ScheduleTypeListCreate(generics.ListCreateAPIView):

    queryset = m.ScheduleType.objects.all()

    def get_serializer_class(self):
        match self.request.method:
            case 'GET':
                return s.ScheduleTypeList
            case 'POST':
                return s.ScheduleTypeCreate
        return None


class ScheduleTypeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = m.ScheduleType.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        match self.request.method:
            case 'GET':
                return s.ScheduleTypeRetrieve
            case 'PUT' | 'PATCH':
                return s.ScheduleTypeUpdate
        return None


# schedule


class ScheduleListCreate(generics.ListCreateAPIView):

    queryset = m.Schedule.objects.all()

    def get_serializer_class(self):
        match self.request.method:
            case 'GET':
                return s.ScheduleList
            case 'POST':
                return s.ScheduleCreate
        return None


class ScheduleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = m.Schedule.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        match self.request.method:
            case 'GET':
                return s.ScheduleRetrieve
            case 'PUT' | 'PATCH':
                return s.ScheduleUpdate
        return None


# task


class TaskListCreate(generics.ListCreateAPIView):

    queryset = m.Task.objects.all()

    def get_serializer_class(self):
        match self.request.method:
            case 'GET':
                return s.TaskList
            case 'POST':
                return s.TaskCreate
        return None

    # if the task doesn't have a schedule, create one and assigned to it
    def perform_create(self, serializer):
        schedule = serializer.data.get('schedule')

        if schedule:
            return serializer.save()

        schedule = m.Schedule().save()

        return serializer.save(schedule=schedule)


class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = m.Task.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        match self.request.method:
            case 'GET':
                return s.TaskRetrieve
            case 'PUT' | 'PATCH':
                return s.TaskUpdate
        return None
