from django.db import models

class blog(models.Model):
    judul = models.CharField(max_length=100)
    penulis = models.CharField(max_length=40)
    penerbit = models.CharField(max_length=40)

    def __str__(self):
        return self.judul

