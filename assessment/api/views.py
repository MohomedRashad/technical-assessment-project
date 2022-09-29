from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer

# view for registering users


class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data)

#Job crud api endpoints
@api_view(['GET'])
def JobOverview(request):
    api_urls = {
        'all_jobs': '/',
        'Search by Job Name': '/?job=job_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/job/pk/delete'
    }
    return Response(api_urls)