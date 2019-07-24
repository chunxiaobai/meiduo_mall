from django.db.models import Model
from django.shortcuts import render

# Create your views here.


class Demo(Model):
    def get(self):
        return 'index'