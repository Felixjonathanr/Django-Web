from django.db import models
from PIL import Image

# Create your models here.

class Bikin_akun(models.Model):
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username

class Produk(models.Model):
    nama_barang = models.CharField(max_length=100)
    harga_barang = models.IntegerField()
    stok_barang = models.IntegerField()
    deskripsi_barang = models.TextField()
    gambar_barang = models.ImageField(upload_to='Produk1')
    kategori_barang = models.CharField(max_length=100)
    seller = models.ForeignKey(Bikin_akun, on_delete=models.CASCADE, related_name='jual_barang')

    def __str__(self):
        return f"{self.seller.username} + {self.nama_barang}"