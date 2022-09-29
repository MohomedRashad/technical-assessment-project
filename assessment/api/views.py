from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import JobHistory
from .serializers import JobSerializer
from .serializers import JobHistorySerializer
from rest_framework import status

# view for registering users
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# Job crud api endpoints
@api_view(['GET'])
def JobOverview(request):
    api_urls = {
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/job/pk/delete'
    }
    return Response(api_urls)


@api_view(['POST'])
def add_jobs(request):
    job = JobSerializer(data=request.data)

    # validating for already existing data
    if Job.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if job.is_valid():
        job.save()
        return Response(job.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_jobs(request, pk):
    job = Job.objects.get(pk=pk)
    data = JobSerializer(instance=job, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_jobs(request, pk):

    job = get_object_or_404(Job, pk=pk)

    job.delete()

    return Response(status=status.HTTP_202_ACCEPTED)

# Job history crud api endpoints
@api_view(['GET'])
def JobHistoryOverview(request):
    api_urls = {
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/jobhistory/pk/delete'
    }
    return Response(api_urls)

@api_view(['POST'])
def add_job_history(request):
    job_history = JobHistorySerializer(data=request.data)

    # validating for already existing data
    if JobHistory.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if job_history.is_valid():
        job_history.save()
        return Response(job_history.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_job_history(request, pk):
    job_history = JobHistory.objects.get(pk=pk)
    data = JobHistorySerializer(instance=job_history, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_job_history(request, pk):
    job_history = get_object_or_404(JobHistory, pk=pk)
    job_history.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
