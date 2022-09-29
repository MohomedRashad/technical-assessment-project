from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

#User model.
class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    user_id = models.BigAutoField(primary_key=True)
    username = None
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length = 100, unique=True)
    date_joined = models.DateField(default=timezone.now)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name
    
#jobs model
class Job(models.Model):
    job_id = models.BigAutoField(primary_key=True)
    job_poster_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Job_name = models.CharField(max_length=200)
    job_description = models.TextField(blank=True,null=True)
    posted_date = models.DateField(default=timezone.now)
    current_status = models.IntegerField(default=1)

    def __str__(self):
        return self.Job_name

#assigned_interviewers model
class AssignedInterviewer(models.Model):
    assigned_interviewer_id = models.BigAutoField(primary_key=True)
    interviewer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)

#job_candidates model
class JobCandidate(models.Model):
    job_candidate_id = models.BigAutoField(primary_key=True)
    candidate_id = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)

#questions model
class Question(models.Model):
    question_id = models.BigAutoField(primary_key=True)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=100)
    question_description = models.CharField(max_length=1000)
    question_category = models.CharField(max_length=50)
    question_alternative_number = models.IntegerField(default=1)

    def __str__(self):
        return self.question_title

#question_assessors model
class QuestionAssessor(models.Model):
    question_assessor_id = models.BigAutoField(primary_key=True)
    assessor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)

#question_assessments model
class QuestionAssessment(models.Model):
    question_assessment_id = models.BigAutoField(primary_key=True)
    question_assessor_id  = models.ForeignKey(User, on_delete=models.CASCADE)
    job_candidate_id = models.ForeignKey(JobCandidate, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
assessment_type = models.CharField(max_length=50)
obtained_score = models.IntegerField(default=0)

#job_history model
class JobHistory(models.Model):
    job_history_id = models.BigAutoField(primary_key=True)
    job_candidate_id = models.ForeignKey(JobCandidate, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    work_place = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.position

