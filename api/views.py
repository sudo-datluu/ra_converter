from rest_framework.response import Response
from .models import FileUpload
from .serializers import FilesSerializer
from rest_framework import viewsets, status
# Create your views here.

class FilesViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FilesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)