from django.db.models import fields
from rest_framework import serializers
from .models import User
from .models import Job
from .models import JobHistory

# UserSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
    fields = ["user_id", "email", "first_name",
              "last_name", "password", "date_joined"]

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# JobSerializer
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('job_poster_id', 'Job_name', 'job_description')

# JobHistorySerializer
class JobHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobHistory
        fields = ('job_candidate_id', 'position', 'work_place','start_date','end_date')
