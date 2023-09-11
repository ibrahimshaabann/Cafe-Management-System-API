from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')



urlpatterns = [
    path('', include(router.urls)), 
    path('token/', TokenObtainPairView.as_view()) # saba7 el foll, u forgot to put the () in as_view
]

# urlpatterns = [
#     path('users/', UserViewSet.as_view(
#           {
#              'get': 'list',
#              'post': 'create'
          
#         }
#         )   
#         ),
# ]