from django.db import models

class Barcode(models.Model):
    code = models.CharField(max_length=13, unique=True)
    image = models.ImageField(upload_to='barcodes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

