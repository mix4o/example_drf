from django.urls import path
from .views import apis, upload

app_name = 'testapp'

urlpatterns = [
    path('api/<int:pk>', apis.api.as_view(), name="api"),
    # path('upload/', upload.uploadFile, name="upload"),
    path('upload/', upload.Upload.as_view(), name='upload'),
    path('upload_complete/', upload.UploadComplete.as_view(), name='upload_complete'),
    path('rest_upload/', apis.UploadFileAPI.as_view(), name='rest_upload'),
    path('rest_upload_filelist/', apis.UploadFilelistAPI.as_view(), name='rest_upload_filelist'),
]
