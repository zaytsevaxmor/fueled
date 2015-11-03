from rest_framework import serializers

from api.models import Restaurant, Review
from django.contrib.auth.models import User, Group


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group