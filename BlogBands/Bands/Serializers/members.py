from rest_framework import serializers
from Bands.models import Members


class MembersBandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Members
        fields = ['id','firstname','surname']