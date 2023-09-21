from django.shortcuts import render
from .models import Benefits,Costs
from .serializers import BenefitsSerializer,CostsSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.filters import  SearchFilter
from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import AdminOnly,IsUserPOST
from .filters import CostsFilter

# from rest_framework.pagination import PageNumberPagination


class BenefitsApiView(ModelViewSet):
    serializer_class = BenefitsSerializer
    queryset = Benefits.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminOnly]
    

    
class CostsApiView(ModelViewSet):
    serializer_class = CostsSerializer
    queryset = Costs.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserPOST]
    filterset_class = CostsFilter
    filter_backends = (SearchFilter, DjangoFilterBackend, )

    def get_queryset(self):
        queryset = self.queryset
        print(queryset.values())
        return queryset

    
    