from rest_framework import serializers
from Bands.models import Categories, Bands, Instruments, Members
# from Bands.serializers2 import BandsSerializer


# class BandsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = bands
#         fields =['name', 'age']

class CategoriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name_categorie']

class BandsSerializer(serializers.ModelSerializer):
    #  categoria = serializers.CharField(source='bandsc.name', read_only=True)

    class Meta:
        model = Bands
        fields =['id','name', 'age', 'img']

class BandsNameSerializer(serializers.ModelSerializer):
    #  categoria = serializers.CharField(source='bandsc.name', read_only=True)

    class Meta:
        model = Bands
        fields =['id', 'name']


class CategoriesSerializer(serializers.ModelSerializer):
    bands = BandsSerializer(many=True)

    class Meta:
        model = Categories
        fields = ['id','name_categorie','bands']

class IntrumentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instruments
        fields = ['id', 'name']

class MembersSerializer(serializers.ModelSerializer):
    bands = BandsSerializer(many=True)
    instruments = IntrumentsSerializer(many=True)

    class Meta:
        model = Members
        fields = ['id', 'firstname', 'surname', 'bands', 'instruments']

class MembersSerializerBasic(serializers.ModelSerializer):

    class Meta:
        model = Members
        fields = ['id', 'firstname', 'surname']


