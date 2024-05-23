# -*- coding: utf-8 -*-
import os
import json
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.services import Services


services = Services()

@api_view(['POST'])
def predict_model(request, *args, **kwargs):
    body = request.body
    dict_body = json.loads(body)
    
    if body != None: 
    
        response = {
            'predict':  services.predict_individual_model(dict_body)
        }
            
        return Response(response, status=200)
        
    return Response({'msg': 'Please inform the body parameters to take the response'}, status=422)
