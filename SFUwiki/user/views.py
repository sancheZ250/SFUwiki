from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.serializers import UserProfileSerializer


class IsModeratorAPI(APIView):
    def get(self, request):
        superuser_status = request.user.is_authenticated and request.user.is_superuser
        admin_status = request.user.is_authenticated and request.user.is_staff
        return Response({'is_superuser': superuser_status, 'is_admin': admin_status}, status=status.HTTP_200_OK)


class AvatarUploadView(APIView):
    def put(self, request, *args, **kwargs):
        profile = request.user.profile
        serializer = UserProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            profile.save