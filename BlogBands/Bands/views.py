from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from User.autorization_mixin import AuthenticationCustom
from Bands.models import Bands, Categories, Members, Instruments
from Bands.serializers import BandsSerializer, CategoriesSerializer, CategoriesListSerializer, MembersSerializer, BandsNameSerializer

# Create your views here.

#
class BandsAPIView(APIView):

    #Lista todos los registros de bandas.
    def get(self, request):
        bands_all = Bands.objects.all()
        bands_serializer = BandsSerializer(bands_all, many = True)
        return Response(data=bands_serializer.data, status=status.HTTP_200_OK)

    #Crea un registro de la banda y se le asigna una categoria por el id de la categoria.
    def post(self, request):
        #category = Categories.objects.get(pk=request.data['id'])
        exist_band = Bands.objects.filter(name=request.data['name'])
        print(request.data)
        if len(exist_band) == 0:
            serializer_band = BandsSerializer(data=request.data)
            if serializer_band.is_valid():
                serializer_band.save()
            else:
                return Response({'error':'estructura de datos incorrecta'}, status= status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'status': 200, 'message':'La banda ya está registrada'})

        # band = Bands.objects.all().last()
        # category.bands.add(band)
        # category.save()
        return Response(serializer_band.data)
    
    def delete(self,request):
        delete_band = Bands.objects.filter(pk=request.data['id']).first()
        delete_band.delete()
        return Response(
            {
                'message': 'Banda eliminada'
            },
            status= status.HTTP_200_OK
        )

class Bands_detail_view(APIView):
    #Lista una banda por su id
    def get(self, request, pk=None):
        band_detail = Bands.objects.filter(id=pk).first()
        band_serializer = BandsSerializer(band_detail)
        return Response(data=band_serializer.data,status=status.HTTP_200_OK)

class GetBandsAlphabetic(APIView):
    def get(self, request, alphabetic):
        bandsAlphabetic = Bands.objects.filter(name__istartswith=alphabetic)
        serializer = BandsNameSerializer(bandsAlphabetic, many=True)

        return Response(serializer.data)


class Band_update_view(APIView):
    #Update band registration by their id
    def put(self, request, pk=None, format=None):
        band_update = Bands.objects.filter(id=pk).first()
        band_serializer = BandsSerializer(band_update, data=request.data)
        if band_serializer.is_valid():
            band_serializer.save()
            print(request.data)
            return Response(band_serializer.data)
        return Response(band_serializer.errors)


class Categories_band_view(APIView):
    #List all categories
    def get(self,request, pk):
        allBands = Categories.objects.get(pk=pk)
        serializer = CategoriesSerializer(allBands)
        return Response(serializer.data)
    
    #Delete a category by id
    def delete(self, request, pk):
        delete_category = Categories.objects.get(pk=pk)
        delete_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Categories_band_create_view(APIView):
    #List all categories
    def get(self,request):
        allBands = Categories.objects.all()
        serializer = CategoriesListSerializer(allBands,many = True)
        return Response(serializer.data)


class Bands_categories(APIView):

    def get(self, request,pk):
        allCategories = Categories.objects.get(pk=pk)
        serializer = BandsSerializer(allCategories.bands, many=True)
        return Response(serializer.data)

class Members_band(APIView):
    def get(sefl, request, pk=None):
        members_band = Members.objects.filter(bands__id=pk)
        serializer = MembersSerializer(members_band, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)