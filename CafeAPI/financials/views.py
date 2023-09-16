from django.shortcuts import render
from .models import Benefits,Costs
from .serializers import BenefitsSerializer,CostsSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import BasePermission
from .permissions import AdminOnly,IsUserPOST

class BenefitsApiView(ModelViewSet):
    serializer_class = BenefitsSerializer
    queryset = Benefits.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [AdminOnly]
    # filter_backends = (DjangoFilterBackend)
    

class CostsApiView(ModelViewSet):
    serializer_class = CostsSerializer
    queryset = Costs.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsUserPOST]
    # filter_backends = (SearchFilter)
    search_fields = ['description']
    