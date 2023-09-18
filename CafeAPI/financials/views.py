from django.shortcuts import render
from .models import Benefits,Costs
from .serializers import BenefitsSerializer,CostsSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.filters import  SearchFilter
from rest_framework.permissions import BasePermission
from .permissions import AdminOnly,IsUserPOST
from .filters import CostsFilter
# from rest_framework.pagination import PageNumberPagination


class BenefitsApiView(ModelViewSet):
    serializer_class = BenefitsSerializer
    queryset = Benefits.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [AdminOnly]
    

# class standardPagination(PageNumberPagination):
#     page_size = 20
#     page_query_param = 'page_size'
#     max_page_size = 30
    
class CostsApiView(ModelViewSet):
    serializer_class = CostsSerializer
    queryset = Costs.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsUserPOST]
    filterset_class = CostsFilter
    filter_backends = (SearchFilter, DjangoFilterBackend, )
    search_fields = ['description']
    # pagination_class = standardPagination

    def get_queryset(self):
        queryset = self.queryset
        print(queryset.values())
        return queryset

    
    