from django.urls import path
from .views import RegisterView
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register/', RegisterView.as_view(), name="sign_up"),
    path('job', views.JobOverview, name='jobs-home'),
    path('job/create/', views.add_jobs, name='add-job'),
    path('job/update/<int:pk>/', views.update_jobs, name='update-job'),
path('job/<int:pk>/delete/', views.delete_jobs, name='delete-job'),
    path('jobhistory', views.JobHistoryOverview, name='job-history-home'),
    path('jobhistory/create/', views.add_job_history, name='add-job-history'),
    path('jobhistory/update/<int:pk>/', views.update_job_history, name='update-job-history'),
path('jobhistory/<int:pk>/delete/', views.delete_job_history, name='delete-job-history'),
]
