from django.db import models

class FileUpload(models.Model):
    fileID = models.AutoField(primary_key=True)
    content = models.FileField(upload_to='store/files/')

    def __str__(self):
        return self.content.name
    
class ColumnType(models.Model):
    columnTypeID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name


class Column(models.Model):
    columnID = models.AutoField(primary_key=True)
    file = models.ForeignKey(FileUpload, on_delete=models.CASCADE)
    column_type = models.ForeignKey(ColumnType, on_delete=models.CASCADE)
