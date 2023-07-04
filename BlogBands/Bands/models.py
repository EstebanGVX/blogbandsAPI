from django.db import models

class Bands(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    img = models.ImageField(upload_to='bands', null=True)

    class Meta:
        db_table = 'bands'
        ordering = ['name']


class Instruments(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'instruments'

class Members(models.Model):
    firstname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    bands = models.ManyToManyField(Bands, related_name='bandsm')
    instruments = models.ManyToManyField(Instruments, related_name='instruments')

    class Meta:
        db_table = 'members'
        ordering = ['firstname']


class Categories(models.Model):
    name_categorie = models.CharField(max_length=30)
    bands = models.ManyToManyField(Bands, related_name='bandsc')

    class Meta:
        db_table = 'categories'
        ordering = ['name_categorie']


# class bands_categories(models.Model):
#     Band = models.ForeignKey(bands, on_delete= models.CASCADE, related_name='bands')
#     Category = models.ForeignKey(categories, on_delete= models.CASCADE,related_name='categories')

#     class Meta:
#         db_table = 'bands_categories'


# class bands_members(models.Model):
#     Band = models.ForeignKey(bands, on_delete=models.CASCADE)
#     Member = models.ForeignKey(members, on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'bands_members'

# class members_instruments(models.Model):
#     Member = models.ForeignKey(members, on_delete=models.CASCADE)
#     Instruments = models.ForeignKey(instruments, on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'members_instruments'