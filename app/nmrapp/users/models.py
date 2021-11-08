from django.db import models

# Create your models here.

class StorageInsert(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    parameter_1=models.IntegerField()
    parameter_2=models.IntegerField()
    file_path=models.CharField(max_length=100)
    # can add model.FileField() for uploads here 
    class Meta:
        db_table="storage"


