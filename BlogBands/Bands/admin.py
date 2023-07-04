from django.contrib import admin
from Bands.models import Bands, Categories, Instruments, Members

# Register your models here.
admin.site.register(Bands)
admin.site.register(Categories)
admin.site.register(Instruments)
admin.site.register(Members)