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

    def delete(self, using=None, keep_parents=False):
        # if no has schedules, delete
        if not self.schedules.exists():
            return super().delete(using, keep_parents)

        # else change status tu deleted
        self.status = self.STATUS_DELETED
        self.save()
        # return information for django
        return 0, {self._meta.label: 0}
