# Generated by Django 3.0.8 on 2020-07-21 14:11

import companies.models.company
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to=companies.models.company.company_logo_upload_location),
        ),
        migrations.AlterField(
            model_name='team',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', related_query_name='team', to='companies.Company'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_memberships',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
