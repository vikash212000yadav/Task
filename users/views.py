from users.models import User, Activity
from rest_framework import viewsets
from users.serializers import UserSerializer, ActivitySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('start_time')
    serializer_class = ActivitySerializer
