from .models import job
from .serializers import Jobserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def job_list_api(request):
    all_jobs = job.objects.all()
    data =Jobserializers(all_jobs,many=True).data

    return Response({'data':data})



@api_view(['GET'])
def job_details_api(request,id):
    job_detail=job.objects.get(id=id)
    data =Jobserializers(job_detail).data

    return Response({'data':data})

class JobListApi(generics.ListCreateAPIView):
    queryset = job.objects.all()
    serializer_class=Jobserializers


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=Jobserializers
    queryset = job.objects.all()
    lookup_field='id'

