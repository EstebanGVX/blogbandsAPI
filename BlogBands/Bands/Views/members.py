from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Bands.models import Members
from Bands.serializers import MembersSerializerBasic
from Bands.Serializers.members import MembersBandSerializer



class Members_alphabetic(APIView):

    def get(self,request):
        print(request.GET['word'])
        members = Members.objects.filter(firstname__icontains=request.GET['word'])
        members_serialzer = MembersSerializerBasic(members, many=True)
        return Response(
            data=members_serialzer.data,
            status=status.HTTP_200_OK
        )

class Members_api(APIView):
    def post(self,request):
        '''
            inputs = firstname:str, surname:srt
            output = Instance Member
        '''
        print(request.data)
        member_serializer = MembersBandSerializer(data=request.data)
        if member_serializer.is_valid():
            member_serializer.save()
            return Response(
                data=member_serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            data={'error':'error creating member'},
            status=status.HTTP_400_BAD_REQUEST
        )
    def delete(self,request):
        member = Members.objects.filter(pk=request.data['id']).first()
        
        try:
            verify = member.delete()

            if verify:
                return Response(
                    data={'message': 'deleted member'},
                    status=status.HTTP_200_OK
                )
        except:
            return Response(
                    data={'error': 'error deleting member'},
                    status=status.HTTP_400_BAD_REQUEST
                )
