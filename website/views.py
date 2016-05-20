from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from registration.views import RegistrationView
# from .models import WaterFacilityType, WaterFacility, AggregatedWaterValue


def index(request):
    template = loader.get_template('website/index.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('website/about.html')
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template('website/contact.html')
    return HttpResponse(template.render())


def donate(request):
    template = loader.get_template('website/donate.html')
    return HttpResponse(template.render())


def latest(request):
    template = loader.get_template('website/latest.html')
    return HttpResponse(template.render())