from django.contrib.auth import get_user_model
from django.db import models


def company_logo_upload_location(instance, filename):
    return 'companies/companies/logo/%s' % filename


class Company(models.Model):
    name = models.CharField(max_length=127)
    logo = models.FileField(null=True, blank=True, upload_to=company_logo_upload_location)
    members = models.ManyToManyField(get_user_model(), blank=True, through='companies.CompanyMembership',
                                     related_name='companies')
