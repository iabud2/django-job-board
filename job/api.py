from .models import Job 
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

#using (function based view)
@api_view(['GET'])
def job_list_api(request):
    all_jobs = Job.objects.all()
    data = JobSerializer(all_jobs, many=True).data
    context = {
        'data':data,
    }
    return Response(context)

#using (class bassed view)
class JobListApi(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class =JobSerializer

#using (function based view)

@api_view(['GET'])
def job_detail_api(request, id):
    job_detail = Job.objects.get(id=id)
    data = JobSerializer(job_detail).data
    context = {
        'data': data,
    }
    return Response(context)

#using (class bassed view)

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    lookup_field = 'id'