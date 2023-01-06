from django.db import models

class Koordinat(models.Model):
    nama_penyu = models.CharField(max_length=100, null=True)
    alamat = models.CharField(max_length=100)
    koordinat = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_penyu

class Klasifikasi(models.Model):
    nama_ilmiah = models.TextField(null=True)
    nama_lokal = models.CharField(max_length=100, null=True)
    spesies = models.CharField(max_length=20)
    img = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nama_ilmiah


    
# Create your models here.


    


