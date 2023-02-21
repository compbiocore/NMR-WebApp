from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

upload_storage = FileSystemStorage(location=settings.UPLOAD_ROOT)

# Create your models here for storing data. 

#class Credentials(models.Model):
    #usern=models.CharField(max_length=100, unique=True)
    #pword=models.CharField(max_length=100)
    #class Meta:
        #db_table="nmr_user"
def file_path(instance, filename):
    return '{0}/user_uploaded/{1}'.format(instance.user_name, filename)

class StorageInsert(models.Model):
    user_name=models.CharField(max_length=100, null=True)
    first_name=models.CharField(max_length=100, null=True)
    last_name=models.CharField(max_length=100, null=True)
    folder=models.FileField(upload_to=file_path, storage=upload_storage)


