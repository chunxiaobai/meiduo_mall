from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from django.views import View


class DemoIndex(View):
    def get(self, request):
        return HttpResponse('index')


class RegisterView(View):
    def get(self, request):
       return render('register.html')