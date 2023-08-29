from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *

@api_view(['POST'])
def getLink(request):
    serializer = URLSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        # return Response({'tiny': f'http://localhost:8000/api/{instance.id}'})
        return Response({'tiny': f'https://tinyy.up.railway.app/api/{instance.id}'})
    
def urlMap(request, pk):
    url = get_object_or_404(Url, id=pk)
    return redirect(url.source)