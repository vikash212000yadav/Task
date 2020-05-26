from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    activities = serializers.SerializerMethodField()

    def get_activities(self, request):
        user_activity = Activity.objects.filter(user=request)
        return ActivitySerializer(user_activity, many=True).data

    class Meta:
        model = User
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['start_time', 'end_time', 'user']
