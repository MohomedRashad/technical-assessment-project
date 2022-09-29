# Generated by Django 4.1.1 on 2022-09-29 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Job_name', models.CharField(max_length=200)),
                ('job_description', models.TextField(blank=True, null=True)),
                ('posted_date', models.DateField(default=django.utils.timezone.now)),
                ('current_status', models.IntegerField(default=1)),
                ('job_poster_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobCandidate',
            fields=[
                ('job_candidate_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.job')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('question_title', models.CharField(max_length=100)),
                ('question_description', models.CharField(max_length=1000)),
                ('question_category', models.CharField(max_length=50)),
                ('question_alternative_number', models.IntegerField(default=1)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.job')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAssessor',
            fields=[
                ('question_assessor_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('assessor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.job')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAssessment',
            fields=[
                ('question_assessment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('job_candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jobcandidate')),
                ('question_assessor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.question')),
            ],
        ),
        migrations.CreateModel(
            name='JobHistory',
            fields=[
                ('job_history_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('position', models.CharField(max_length=100)),
                ('work_place', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('job_candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jobcandidate')),
            ],
        ),
        migrations.CreateModel(
            name='AssignedInterviewer',
            fields=[
                ('assigned_interviewer_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('interviewer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.job')),
            ],
        ),
    ]
