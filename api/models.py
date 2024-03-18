from django.db import models

class FileUpload(models.Model):
    fileID = models.AutoField(primary_key=True)
    content = models.FileField(upload_to='store/files/')

    def __str__(self):
        return self.content.name

class Column(models.Model):
    columnID = models.AutoField(primary_key=True)
    file = models.ForeignKey(FileUpload, on_delete=models.CASCADE)
    column_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}: {self.column_type}"