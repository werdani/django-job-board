from .models import job
from .serializers import Jobserializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def joblistapi(request):
    all_jobs = job.objects.all()
    data =Jobserializers(all_jobs,many=True).data

    return Response({'data':data})