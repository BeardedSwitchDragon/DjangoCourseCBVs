from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


class CBView(View):
    def get(self, request):
        return HttpResponse("ClaSs BAsed Views arE cOO0l!!!!!!!!!11!")
