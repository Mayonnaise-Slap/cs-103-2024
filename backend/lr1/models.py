from django.core.validators import MaxValueValidator
from django.db import models

from cs103_backend.models import Student


class StudentLr1Progress(models.Model):
    # Stores student progress
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    # task 1 progress
    GET = models.BooleanField(default=False)
    POST = models.BooleanField(default=False)
    PATCH = models.BooleanField(default=False)
    PUT = models.BooleanField(default=False)
    DELETE = models.BooleanField(default=False)

    @property
    def task_1_finished(self):
        return all([self.GET, self.POST, self.PATCH, self.PUT, self.DELETE])

    # TODO smarter way to track progress, probably with external models
    # TODO how to store random sequences deterministically
    task_2_counter = models.IntegerField(default=0, validators=[MaxValueValidator(101)])
    task_3_counter = models.IntegerField(default=0, validators=[MaxValueValidator(51)])
    task_4_counter = models.IntegerField(default=0, validators=[MaxValueValidator(51)])

