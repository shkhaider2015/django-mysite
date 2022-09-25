from rest_framework.response import Response
from rest_framework.decorators import api_view
from polls.models import Question
from .serializers import QuestionSerializer

@api_view(['GET'])
def get_data(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def post_data(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)