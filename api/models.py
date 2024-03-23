from django.db import models


# Create your models here.
class bin_data(models.Model):
    bin_id = models.AutoField(primary_key=True)
    bin_code = models.CharField(max_length=12)
    bin_country = models.CharField(max_length=100)
    bin_brand = models.CharField(max_length=12)
    bin_type = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.bin_code
