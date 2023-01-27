
# class ScheduleTypeViewSet(viewsets.ModelViewSet):

#     queryset = m.ScheduleType.objects.all()
#     lookup_field = 'uuid'

#     def get_serializer_class(self):
#         match self.action:
#             case 'create':
#                 return s.ScheduleTypeCreate
#             case 'retrieve' | 'list':
#                 return s.ScheduleTypeList
#             case 'update' | 'partial_update':
#                 return s.ScheduleTypeUpdate
#         return None


# class ScheduleViewSet(viewsets.ModelViewSet):

#     queryset = m.Schedule.objects.all()
#     lookup_field = 'uuid'

#     def get_serializer_class(self):
#         match self.action:
#             case 'create':
#                 return s.ScheduleCreate
#             case 'retrieve' | 'list':
#                 return s.ScheduleList
#             case 'update' | 'partial_update':
#                 return s.ScheduleUpdate
#         return None


# class TaskViewSet(viewsets.ModelViewSet):

#     queryset = m.Task.objects.all()
#     lookup_field = 'uuid'

#     def get_serializer_class(self):
#         match self.action:
#             case 'create':
#                 return s.TaskCreate
#             case 'retrieve' | 'list':
#                 return s.TaskList
#             case 'update' | 'partial_update':
#                 return s.TaskUpdate
#         return None
