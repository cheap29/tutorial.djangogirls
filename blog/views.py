from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    Datetime = {
        'hour': datetime.now().hour,
    }
    return render(request, 'index.html', Datetime)