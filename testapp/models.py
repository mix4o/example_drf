from django.db import models


class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Document(models.Model):
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "media/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
