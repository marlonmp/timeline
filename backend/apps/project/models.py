from uuid import uuid4

from django.db import models


class Project(models.Model):
    """
    This model represents a real-life project.
    This model has the basic information project
    and it groups all project task and schedules
    """

    STATUS_PENDING = 'PN'
    STATUS_DEVELOP = 'DV'
    STATUS_FINISHED = 'FN'
    STATUS_REVIEW = 'RV'
    STATUS_DELETED = 'DL'

    CHOICE_STATUS = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_DEVELOP, 'In develop'),
        (STATUS_FINISHED, 'Finished'),
        (STATUS_REVIEW, 'Under review'),
        (STATUS_DELETED, 'Deleted'),
    )


    uuid = models.UUIDField(unique=True, editable=False, default=uuid4)

    title = models.CharField(max_length=80)

    name = models.CharField(max_length=80, unique=True)

    description = models.CharField(max_length=240, blank=True)

    members = models.ManyToManyField('user.User', related_name='projects', blank=True)

    status = models.CharField(max_length=2, choices=CHOICE_STATUS, default=STATUS_PENDING)

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

    project = models.ForeignKey('project.Project', on_delete=models.PROTECT, related_name='schedules', null=True)

    owner = models.ForeignKey('user.User', on_delete=models.PROTECT, related_name='schedules', null=True)

    type = models.ForeignKey('project.ScheduleType', on_delete=models.PROTECT, related_name='schedules')

    description = models.CharField(max_length=240, blank=True)

    status = models.CharField(max_length=2, choices=CHOICE_STATUS, default=STATUS_PENDING)

    created_at = models.DateTimeField(editable=False, auto_now_add=True)


class AbstractTask(models.Model):

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

    description = models.CharField(max_length=240, blank=True)

    const_time = models.DurationField(null=True, blank=True)

    status = models.CharField(max_length=2, choices=CHOICE_STATUS, default=STATUS_PENDING, null=True)

    created_at = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        abstract = True


class Task(AbstractTask):

    owner = models.ForeignKey('user.User', on_delete=models.PROTECT, related_name='tasks', null=True)

    schedule = models.ForeignKey('project.Schedule', on_delete=models.PROTECT, related_name='tasks')

    def save(self, *args, **kwargs):

        attrs = { 'dispatcher': '' }
        fields = ['owner', 'description', 'const_time', 'status']

        for field in fields:
            value = getattr(self, field)
            if value:
                attrs[field] = value

        TaskAction(**attrs).save()

        return super().save(*args, **kwargs)


class TaskAction(AbstractTask):

    owner = models.ForeignKey('user.User', on_delete=models.PROTECT, related_name='assigned_tasks', null=True)

    dispatcher = models.ForeignKey('user.User', on_delete=models.PROTECT, related_name='task_actions')

    task = models.ForeignKey('project.Task', on_delete=models.PROTECT, related_name='task_actions')
