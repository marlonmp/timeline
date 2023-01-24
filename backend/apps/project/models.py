from uuid import uuid4

from django.db import models


class Project(models.Model):
    """
    This model represents a real-life project.
    This model has the basic information project
    and it groups all project task and schedules
    """

    STATUS_ACTIVE = 'AC'
    STATUS_PAUSED = 'PS'
    STATUS_REVIEW = 'RV'
    STATUS_FINISHED = 'FN'
    STATUS_PRODUCTION = 'PR'
    STATUS_DELETED = 'DL'

    CHOICE_STATUS = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_PAUSED, 'Paused'),
        (STATUS_DELETED, 'Deleted'),
    )

    uuid = models.UUIDField(unique=True, editable=False, default=uuid4)

    title = models.CharField(max_length=80)

    name = models.CharField(max_length=80, unique=True)

    description = models.CharField(max_length=240, blank=True)

    members = models.ManyToManyField('user.User', related_name='projects', blank=True)

    status = models.CharField(max_length=2, choices=CHOICE_STATUS, default=STATUS_ACTIVE)

    created_at = models.DateTimeField(editable=False, auto_now_add=True)


class ScheduleType(models.Model):
    """
    This model represents the type of developemt executed in a schema.
    For example: ajustment, requirement, etc.
    """

    uuid = models.UUIDField(unique=True, editable=False, default=uuid4)

    name = models.CharField(max_length=80, unique=True)

    description = models.CharField(max_length=240, blank=True)

    created_at = models.DateTimeField(editable=False, auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


class Schedule(models.Model):
    """
    This model represents a grpup of tasks
    """

    STATUS_ACTIVE = 'AC'
    STATUS_IN_PROGRESS = 'PG'
    STATUS_CLOSED = 'CL'
    STATUS_PAUSED = 'PS'
    STATUS_DELETED = 'DL'

    CHOICE_STATUS = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_IN_PROGRESS, 'In progress'),
        (STATUS_CLOSED, 'Closed'),
        (STATUS_PAUSED, 'Paused'),
        (STATUS_DELETED, 'Deleted'),
    )

    uuid = models.UUIDField(unique=True, editable=False, default=uuid4)

    project = models.ForeignKey('project.Project', on_delete=models.PROTECT, related_name='schedules', null=True)

    owner = models.ForeignKey('user.User', on_delete=models.PROTECT, related_name='schedules', null=True)

    type = models.ForeignKey('project.ScheduleType', on_delete=models.PROTECT, related_name='schedules')

    description = models.CharField(max_length=240, blank=True)

    status = models.CharField(max_length=2, choices=CHOICE_STATUS, default=STATUS_ACTIVE)

    created_at = models.DateTimeField(editable=False, auto_now_add=True)


class Task(models.Model):

    STATUS_ACTIVE = 'AC'
    STATUS_IN_PROGRESS = 'PG'
    STATUS_SOLVED = 'SV'
    STATUS_CLOSED = 'CL'
    STATUS_PAUSED = 'PS'
    STATUS_DELETED = 'DL'

    CHOICE_STATUS = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_IN_PROGRESS, 'In progress'),
        (STATUS_SOLVED, 'Solved'),
        (STATUS_CLOSED, 'Closed'),
        (STATUS_PAUSED, 'Paused'),
        (STATUS_DELETED, 'Deleted'),
    )

    uuid = models.UUIDField(unique=True, editable=False, default=uuid4)

    schedule = models.ForeignKey('project.Schedule', on_delete=models.PROTECT, related_name='tasks')

    owner = models.ForeignKey('user.User', on_delete=models.PROTECT, related_name='tasks', null=True)

    description = models.CharField(max_length=240, blank=True)

    const_time = models.DurationField(null=True)

    status = models.CharField(max_length=2, choices=CHOICE_STATUS, default=STATUS_ACTIVE)

    created_at = models.DateTimeField(editable=False, auto_now_add=True)
