from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def v_view(request):
    now = datetime.datetime.now()
    html = "time is {}".format(now)
    return HttpResponse(html)
