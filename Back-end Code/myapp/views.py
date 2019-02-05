from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
from .model import predict

@csrf_exempt
def index(request):
    if request.method == "POST":
        s = request.body.decode('utf-8')
        text = json.loads(s)['text']
        print(text)
    return HttpResponse(predict(text))
