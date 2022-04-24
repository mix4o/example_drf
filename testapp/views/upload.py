from .. import models
from django.shortcuts import render,redirect
import os
from django.views.generic.edit import FormView
from ..forms import *
from django.conf import settings


def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        file_title = request.POST["fileTitle"]
        uploaded_file = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            title=file_title,
            uploadedFile=uploaded_file
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, os.path.join("testapp", "upload-file.html"), context={
        "files": documents
    })


# ファイルアップロード
class Upload(FormView):
    template_name = 'testapp/upload-file-class.html'
    form_class = UploadFileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.get_form()
        context = {
            'form': form,
        }
        return context

    def form_valid(self, form):
        # handle_uploaded_file(self.request.FILES['file'])
        os.makedirs(settings.UPLOAD_DIR)
        path = os.path.join(settings.UPLOAD_DIR, self.request.FILES['file'].name)
        with open(path, 'wb+') as destination:
            for chunk in self.request.FILES['file'].chunks():
                destination.write(chunk)
        return redirect('testapp:upload_complete')  # アップロード完了画面にリダイレクト


# ファイルアップロード完了
class UploadComplete(FormView):
    template_name = 'testapp/upload_complete.html'
    form_class = UploadFileForm
