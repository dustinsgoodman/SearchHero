from models import *
from django.shortcuts import get_object_or_404, render_to_response, redirect
#from django.http import HttpRequest, HttpResponse
#import time, smtplib, math, urllib2, random, datetime
#from django.template import Context, loader
#import urllib

def home_view(request):
	return render_to_response('home.html')

def help_view(request):
	return render_to_response('help.html')

def game_view(request):
	return render_to_response('game.html')

def stats_view(request):
	return render_to_response('stats.html')

def results_view(request):
	return render_to_response('results.html')

