# Generated by Django 4.2.5 on 2023-11-13 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CurriculumVitae', '0004_remove_curriculumvitae_education_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculumvitae',
            name='education',
        ),
        migrations.RemoveField(
            model_name='curriculumvitae',
            name='interest',
        ),
        migrations.RemoveField(
            model_name='curriculumvitae',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='curriculumvitae',
            name='workexperience',
        ),
        migrations.AddField(
            model_name='curriculumvitae',
            name='education',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CurriculumVitae.education'),
        ),
        migrations.AddField(
            model_name='curriculumvitae',
            name='interest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CurriculumVitae.interests'),
        ),
        migrations.AddField(
            model_name='curriculumvitae',
            name='skills',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CurriculumVitae.skills'),
        ),
        migrations.AddField(
            model_name='curriculumvitae',
            name='workexperience',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CurriculumVitae.workexperience'),
        ),
    ]