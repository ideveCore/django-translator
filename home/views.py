import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import translators as ts


def home(request):
    return render(request, 'home.html')


@api_view(['POST'])
def translate(request):
    if request.method == 'POST':
        input = json.loads(request.body.decode('utf-8'))['input']
        from_language = json.loads(request.body.decode('utf-8'))['from']
        to_language = json.loads(request.body.decode('utf-8'))['to']
        if input == '':
            content = {'error': 'Empty input!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            output = ts.translate_text(
                input, from_language=from_language, to_language=to_language)
            content = {'output': output}
            return Response(content, status=status.HTTP_200_OK)
    return JsonResponse({'error': 'Unexpected error!'})
