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
        requestData = serializers.serialize('json', list(objectQuerySet), fields=('id', 'name', 'publish', 'data'))  
        data = json.loads(requestData)
        # print(data[0]['fields']['data']['data'][0]['data'])
        
        # delete unpublished quizzes
        for qi, quiz in enumerate(data):
            if quiz['fields']['publish'] == False:
                del data[qi]
        
        # foreach quiz
        for qi, quiz in enumerate(data): 
            
            # foreach stepper in quiz
            for di, step in enumerate(quiz['fields']['data']['data']):
                # foreach question in stepper
                for si, stepQ in enumerate(step['data']):
                    # if answer key in object delete it
                    if 'answer' in stepQ:
                        del data[qi]['fields']['data']['data'][di]['data'][si]['answer']
        # return santised object to client
        return Response(data)
class QuizSubmission(APIView):
    """
    post: validates quiz submission
    """
    
    def post(self, request, quiz_id):
        
        quiz = InductionQuizzes.objects.get(pk=quiz_id).data['data']
        print(quiz[0]['data'])
        formResults = {}
        
        for step in quiz:
            for stepQ in step['data']:
                if 'id' in stepQ:
                 print(stepQ['id'])
                 if stepQ['answer'].lower() == 'true':
                    formResults[stepQ['id']] = True
                 else:
                    if stepQ['answer'].lower() == 'false':
                        formResults[stepQ['id']] = False
                    else:
                        formResults[stepQ['id']] = stepQ['answer']
                    
        print(formResults)
        print(request.data)
        print(quiz_id)
        
        if formResults == request.data:
            print(True)
            return Response({'result':'competent'})

        else: 
            print(False) 
            return Response({'result':'incompetent'})
        