from rest_framework import serializers
from vendor.models import VendorProfile
from django.contrib.auth.models import User


class AdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"], password=validated_data["password"]
        )
        return user

    class Meta:
        model = User
        fields = ["username", "password"]


class VendorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = '__all__'

