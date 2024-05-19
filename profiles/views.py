from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from django.http import Http404
from django.views import generic
from django.urls import reverse_lazy

from . import models, serializers
# Create your views here.

class MyModelListApiView(APIView):
    def get(self, request, format=None):
        mymodel = models.Profile.objects.all()
        serializer = serializers.MySerializer(mymodel, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.MySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MyModelDetailApiView(APIView):
    def get_object(self, mymodel_id):
        try:
            return models.Profile.objects.get(pk=mymodel_id)
        except models.MyModel.DoesNotExist:
            raise Http404

    def get(self, request, mymodel_id, format=None):
        mymodel = self.get_object(mymodel_id)
        serializer = serializers.MySerializer(mymodel)
        return Response(serializer.data)
    