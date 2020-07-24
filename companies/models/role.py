from django.db import models


class Role(models.Model):
    MEMBER = 0
    MANAGER = 1
    OWNER = 2
    ACCESS_CHOICES = (
        (MEMBER, 'Member'),
        (MANAGER, 'Manager'),
        (OWNER, 'Owner'),
    )
    name = models.CharField(max_length=32)
    access = models.FloatField(choices=ACCESS_CHOICES, default=MEMBER)
