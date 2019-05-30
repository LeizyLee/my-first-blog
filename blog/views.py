from django.http import JsonResponse
import json
import sys
from ctModule import NWparse
# Create your views here.
def get_webtoonlink():


    __author__ = 'lsy2sy'
    print(sys.stdin.encoding)
    data = NWparse.get_nwlinke()
    return data

def post_list(request):
    return JsonResponse(get_webtoonlink(), safe=False)
