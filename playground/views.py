from django.shortcuts import render
from rest_framework.views import APIView
import requests


# Create your views here.
class SayHello(APIView):
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        return render(request, 'hello.html', {'name': 'Aaron'})