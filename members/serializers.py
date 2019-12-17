from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)