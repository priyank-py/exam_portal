from rest_framework import serailizers
from members.models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['user', 'about', 'image']
        
    
