from rest_framework import serializers
from Bands.models import Bands



# class BandsSerializer(serializers.ModelSerializer):

#     categoria = CategoriesListSerializer(source='id', read_only=True, many=True)

#     class Meta:
#         model = Bands
#         fields =['id', 'name', 'age', 'img', 'categoria']
