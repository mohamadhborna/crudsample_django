from django.db import models
from django.contrib.auth import get_user_model


class Team(models.Model):
    name = models.CharField(max_length=32)
    company = models.ForeignKey(
        to='companies.Company',
        related_name='teams',
        related_query_name='team',
        on_delete=models.CASCADE
    )
    team_memberships = models.ManyToManyField(to=get_user_model(), blank=True)
