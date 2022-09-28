from django.contrib import admin
from .models import User
from .models import Job
from .models import AssignedInterviewer
from .models import JobCandidate
from .models import Question
from .models import QuestionAssessor
from .models import QuestionAssessment
from .models import JobHistory

admin.site.register(User)
admin.site.register(Job)
admin.site.register(AssignedInterviewer)
admin.site.register(JobCandidate)
admin.site.register(Question)
admin.site.register(QuestionAssessor)
admin.site.register(QuestionAssessment)
admin.site.register(JobHistory)
#admin.site.register()
#admin.site.register()
#admin.site.register()
#admin.site.register()
