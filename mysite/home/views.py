# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

# def index(request):
#     return render_to_response('home/index.html')

# def index(request):
#      return HttpResponse("Coming Soon!")

# class HomePageView(TemplateView):
#     def get(self, request, **kwargs):
#         return render(request, 'index.html', context=None)

def index(request):
    return render(request, 'home/index.html', context=None)
