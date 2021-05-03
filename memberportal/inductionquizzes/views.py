from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from constance import config
from inductionquizzes.models import InductionQuizzes
import pytz
import json
from django.http import JsonResponse
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, YourCustomType):
            return str(obj)
        return super().default(obj)

utc = pytz.UTC

class Inductionquiz(APIView):
    """
    get: returns published quizzes
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request):

        objectQuerySet = InductionQuizzes.objects.all()
        data = serializers.serialize('json', list(objectQuerySet), fields=('id', 'name', 'publish', 'data'))        
        print(json.loads(data))
        return Response(json.loads(data))
    