#!/usr/bin/env python
# coding=utf-8
from django.views.generic import View
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
from django import forms


def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def the_site(request):
    form = request.POST
    print form
    return render(request, 'index.html', {'form': form})

def nutricion(request):
    now = datetime.datetime.now()
    t = get_template('nutricion.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def que_es(request):
    now = datetime.datetime.now()
    t = get_template('que_es.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def sobre_nosotros(request):
    now = datetime.datetime.now()
    t = get_template('sobre_nosotros.html')
    html = t.render(Context({}))
    return HttpResponse(html)


class ProcessImage(View):
    def post(self, request):
        print "entro"
        foto = request.POST['foto']
        result = clarifai_api.tag_images(foto)
        print "test"
        print result
        return HttpResponse(result)
