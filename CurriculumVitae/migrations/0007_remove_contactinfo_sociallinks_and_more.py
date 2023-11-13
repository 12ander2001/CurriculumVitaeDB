# Generated by Django 4.2.5 on 2023-11-13 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CurriculumVitae', '0006_remove_curriculumvitae_education_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='sociallinks',
        ),
        migrations.AddField(
            model_name='sociallinks',
            name='contact_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='social_links', to='CurriculumVitae.contactinfo'),
        ),
    ]
