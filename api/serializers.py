from rest_framework import serializers
from .models import FileUpload

class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = '__all__'

    def validate_content(self, value):
        """
        Check that the uploaded file is a CSV or Excel file.
        """
        file_extension = value.name.split('.')[-1]
        if file_extension not in ['csv', 'xlsx', 'xls']:
            raise serializers.ValidationError("Invalid file type. Only 'csv' and 'xlsx/xls' are allowed.")
        return value