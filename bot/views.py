from django.shortcuts import render

from bitstampApi import bitstamp
# Create your views here.

def index(request):
    api = bitstamp.Bitstamp('bitstampApi/config.py')
    print(api.ticker())
    context = {}
    return render(request, 'bot/index.html', context)

