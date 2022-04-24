from ..models import SampleModel  # モデル呼出
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, GenericAPIView  # API
from ..serializers import SampleSerializer  # APIで渡すデータをJSON,XML変換
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, ParseError
from django.conf import settings
import os


class api(RetrieveAPIView):
    # 対象とするモデルのオブジェクトを定義
    queryset = SampleModel.objects.all()

    # APIがデータを返すためのデータ変換ロジックを定義
    serializer_class = SampleSerializer

    # 認証
    permission_classes = []


class UploadFileAPI(GenericAPIView):
    parser_classes = [FormParser, MultiPartParser]

    def get(self, request, *args, **kwargs):
        os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
        filelist = [name for name in os.listdir(settings.UPLOAD_DIR)]
        return JsonResponse({'filelist': filelist})

    def post(self, request, *args, **kwargs):
        try:
            file = request.data['file']
            os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
            path = os.path.join(settings.UPLOAD_DIR, file.name)
            with open(path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        except KeyError:
            raise ParseError('Request has no resource file attached')
        return JsonResponse({}, status=status.HTTP_201_CREATED)


class UploadFilelistAPI(GenericAPIView):
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        try:
            filelist = request.data['filelist']
        except KeyError:
            raise ParseError('Request has no filelist')
        return JsonResponse({}, status=status.HTTP_200_OK)
