from django.utils import timezone
from django.db import models

# user model
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length = 100)
    password = models.CharField(max_length=100)
    registered_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.first_name + self.last_name

#jobs model
class Job(models.Model):
    job_id = models.BigAutoField(primary_key=True)
    job_poster_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Job_name = models.CharField(max_length=200)
    job_description = models.CharField(max_length=1000)
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

