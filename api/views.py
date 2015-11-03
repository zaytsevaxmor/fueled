from django.shortcuts import render_to_response
from django.contrib.auth.models import User, Group
from api.models import Restaurant
from api.serializers import UserSerializer, GroupSerializer, RestaurantSerializer
from rest_framework import permissions, viewsets
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


def index(request):
    return render_to_response('index.html')

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
#    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
