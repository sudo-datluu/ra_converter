from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import FilesViewSet, ColumnViewSet

router = SimpleRouter()
router.register(r'files', FilesViewSet, basename='files')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/files/<int:file_id>/columns/', ColumnViewSet.as_view({'get': 'list'})),
]
