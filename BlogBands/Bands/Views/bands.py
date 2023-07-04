from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from Bands.models import Bands, Categories, Members, Instruments
from Bands.serializers import BandsSerializer, CategoriesListSerializer
from Bands.Serializers.members import MembersBandSerializer
from User.autorization_mixin import AuthenticationCustom
import json


class GetDataBand(APIView):
    def get(self,request,id):
        band = Bands.objects.get(pk=id)
        band_serializer = BandsSerializer(band)
        category = band.bandsc.all()
        category_serializer = CategoriesListSerializer(category, many=True)
        members = band.bandsm.all()
        members_serializer = MembersBandSerializer(members, many=True)

        return Response(
            data={
                'band':band_serializer.data, 
                'categories': category_serializer.data, 
                'members':members_serializer.data
            },
            status=status.HTTP_200_OK,
        )

    def put(self,request,id):
        band = Bands.objects.filter(pk=request.data['id']).first()
        band_serializer = BandsSerializer(band,data=request.data)

        if band_serializer.is_valid():
            band_serializer.save()
        else:
            return Response(
                {
                    'error': 'datos invalidos'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return Response(data=band_serializer.data, status=status.HTTP_200_OK)

class EditBand(APIView):

    def put(self, request):
        print(request.data)
        data_members = json.loads(request.data['members'])
        data_band = {
            'name': request.data['name'],
            'age': request.data['age']
        }
        if request.data['img'] != 'null' and request.data['img'] != '':
            data_band['img'] = request.data['img']
        print(type(request.data['img']))
        print(type(data_members))
        
        band = Bands.objects.filter(pk=request.data['id']).first()
        band_serializer = BandsSerializer(band,data=data_band,partial=True)

        if band_serializer.is_valid():
            band_serializer.save()
        else:
            return Response(data={'error':'failed to update'}, status=status.HTTP_400_BAD_REQUEST)

        for key, value in data_members.items():
            if len(value) != 0:
                if key == 'add':
                    for memberToAdd in value:
                        member = Members.objects.filter(pk=memberToAdd['id']).first()
                        band.bandsm.add(member)
                if key == 'delete':
                    for memberToAdd in value:
                        member = band.bandsm.filter(pk=memberToAdd['id']).first()
                        band.bandsm.remove(member)
        
        return Response(
            {
                'band': band_serializer.data, 
            },
            status= status.HTTP_200_OK
        )
