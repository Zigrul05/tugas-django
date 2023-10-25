from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def menuutama(request):
    template = loader.get_template('menuutama.html')
    return HttpResponse(template.render())
def kucing(request):
    template = loader.get_template('kucing.html')
    return HttpResponse(template.render())
def burung(request):
    template = loader.get_template('burung.html')
    return HttpResponse(template.render())