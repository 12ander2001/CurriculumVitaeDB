# Generated by Django 4.2.5 on 2023-11-10 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameinst', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('range', models.CharField(max_length=255)),
                ('curse', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('assessment', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('range', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CurriculumVitae',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CurriculumVitae.education')),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CurriculumVitae.interests')),
                ('skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CurriculumVitae.skills')),
                ('workexperience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CurriculumVitae.workexperience')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=255)),
                ('sociallinks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CurriculumVitae.sociallinks')),
            ],
        ),
    ]