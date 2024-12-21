from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Student(AbstractUser):
    isu = models.IntegerField(
        validators=[
            MinValueValidator(100000),
            MaxValueValidator(999999)
        ],
        help_text='Ваш номер ИСУ'
    )
    full_name = models.CharField(max_length=250)
    group_name = models.CharField(max_length=6)

    def save(self, **kwargs):
        self.full_name = self.full_name.strip()
        self.group_name = self.group_name.strip().replace('К', 'K')
        super(Student, self).save(**kwargs)

    def __str__(self):
        return self.full_name