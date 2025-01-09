from rest_framework import viewsets
from .models import User, Hazard
from .serializers import UserSerializer, HazardSerializer

# Define UserViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Define HazardViewSet
class HazardViewSet(viewsets.ModelViewSet):
    queryset = Hazard.objects.all()
    serializer_class = HazardSerializer

# Define HomeAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeAPIView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the API!"})
