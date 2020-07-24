from django.contrib.auth import get_user_model
from django.db import models


class CompanyMembership(models.Model):
    company = models.ForeignKey(to='companies.Company', on_delete=models.CASCADE)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    role = models.ForeignKey(to='companies.Role', on_delete=models.CASCADE)
