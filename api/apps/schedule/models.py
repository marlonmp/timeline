from uuid import uuid4

from django.db import models


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

    STATUS_PENDING = 'PN'
    STATUS_IN_PROGRESS = 'PG'
    STATUS_SOLVED = 'SV'
    STATUS_PAUSED = 'PS'
    STATUS_DELETED = 'DL'

    CHOICE_STATUS = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_IN_PROGRESS, 'In progress'),
        (STATUS_SOLVED, 'Solved'),
        (STATUS_PAUSED, 'Paused'),
        (STATUS_DELETED, 'Deleted'),
    )

    uuid = models.UUIDField(unique=True, editable=False, default=uuid4)

    project = models.ForeignKey('project.Project', on_delete=models.PROTECT, related_name='schedules', null=True, blank=True)

    owner = models.ForeignKey('user.User', on_delete=models.PROTECT, related_name='schedules', null=True, blank=True)

    type = models.ForeignKey('schedule.ScheduleType', on_delete=models.PROTECT, related_name='schedules', null=True, blank=True)

    description = models.CharField(max_length=240, blank=True)

    status = models.CharField(max_length=2, choices=CHOICE_STATUS, default=STATUS_PENDING)

    created_at = models.DateTimeField(editable=False, auto_now_add=True)


class Task(models.Model):

    STATUS_PENDING = 'PN'
    STATUS_IN_PROGRESS = 'PG'
    STATUS_SOLVED = 'SV'
    STATUS_PAUSED = 'PS'
    STATUS_DELETED = 'DL'

    CHOICE_STATUS = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_IN_PROGRESS, 'In progress'),
        (STATUS_SOLVED, 'Solved'),
        (STATUS_PAUSED, 'Paused'),
        (STATUS_DELETED, 'Deleted'),
    )

    uuid = models.UUIDField(unique=True, editable=False, default=uuid4)

    schedule = models.ForeignKey('schedule.Schedule', on_delete=models.PROTECT, related_name='tasks')

    owner = models.ForeignKey('user.User', on_delete=models.PROTECT, related_name='tasks', null=True)

    description = models.CharField(max_length=240, blank=True)

    const_time = models.DurationField(null=True, blank=True)

    status = models.CharField(max_length=2, choices=CHOICE_STATUS, default=STATUS_PENDING, null=True)

    created_at = models.DateTimeField(editable=False, auto_now_add=True)
