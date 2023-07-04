from django.urls import path
from Bands.views import BandsAPIView, Bands_detail_view, Band_update_view, Categories_band_view, Categories_band_create_view,Bands_categories, Members_band, GetBandsAlphabetic
from Bands.Views.bands import GetDataBand, EditBand
from Bands.Views.members import Members_alphabetic, Members_api



urlpatterns = [
    path('band/', BandsAPIView.as_view(), name= 'bands_view'),
    path('<int:pk>/', Bands_detail_view.as_view(), name='band_detail_view'),
    path('update-detail/<int:pk>/',Band_update_view.as_view(), name='band_update_view'),
    path('categories-list/', Categories_band_create_view.as_view(), name='Categories_band_create_view'),
    path('allBands/categories/<int:pk>', Bands_categories.as_view(), name='categories_band_view'),
    path('band/members/<int:pk>', Members_band.as_view(), name='Members_band'),
    path('alphabetic/<str:alphabetic>', GetBandsAlphabetic.as_view(), name='GetBandsAlphabetic'),
    path('get-band/<int:id>',GetDataBand.as_view(), name='GetDataBand'),
    path('members/alphabetic',Members_alphabetic.as_view(), name='Members_alphabetic'),
    path('editband/', EditBand.as_view(), name='EditBand'),
    path('members/createMember/', Members_api.as_view(), name='Members_api'),
]