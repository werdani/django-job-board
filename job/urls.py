from django.urls import include,path
from . import views,api
app_name = 'job'


urlpatterns = [
    path('',views.job_list ,name='job_list'),
    path('add',views.add_job , name='add_job'),
    path('<str:slug>',views.job_detail , name='job_detail'),
    #api
    path('api/jobs',api.job_list_api , name='job_list_api'),
    path('api/jobs/<int:id>',api.job_details_api , name='job_details_api'),

    #class based viwes
    path('api/v2/jobs',api.JobListApi.as_view() , name='JobListApi'),
    path('api/v2/jobs/<int:id>',api.JobDetail.as_view() , name='job_details_api'),



    
]