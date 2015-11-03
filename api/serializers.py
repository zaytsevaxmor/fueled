from rest_framework import serializers

from api.models import Restaurant
from django.contrib.auth.models import User, Group


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group