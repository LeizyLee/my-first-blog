from django.http import JsonResponse
from django.shortcuts import render
import urllib.request
from bs4 import BeautifulSoup

# Create your views here.
def get_webtoonlink():


    __author__ = 'lsy2sy'

    html = urllib.request.urlopen('http://comic.naver.com/webtoon/weekday.nhn')  # 웹툰 사이트를 엶
    soup = BeautifulSoup(html, features="html.parser")  # 사이트를 파싱해서 가져옴
    titles = soup.find_all("a", "title")  # 가져온 데이터를 find_all 메소드를 이용해서 a 속성의 b 클래스를 찾는다
    weekdays = soup.find_all("h4")  # 요일을 찾기위해 h4 속성을 찾는다

    # print(titles)
    mondic = {}
    tuedic = {}
    weddic = {}
    thudic = {}
    fridic = {}
    satdic = {}
    sundic = {}
    for i in titles:
        link = i.get('href')
        name = i.get('title')
        if 'mon' in link:
            mondic[name] = 'http://comic.naver.com' + link[:32]
        elif 'tue' in link:
            tuedic[name] = 'http://comic.naver.com' + link[:32]
        elif 'wed' in link:
            weddic[name] = 'http://comic.naver.com' + link[:32]
        elif 'thu' in link:
            thudic[name] = 'http://comic.naver.com' + link[:32]
        elif 'fri' in link:
            fridic[name] = 'http://comic.naver.com' + link[:32]
        elif 'sat' in link:
            satdic[name] = 'http://comic.naver.com' + link[:32]
        elif 'sun' in link:
            sundic[name] = 'http://comic.naver.com' + link[:32]

    import json
    tmp = {}
    tmp['월요 웹툰'] = mondic
    tmp['화요 웹툰'] = tuedic
    tmp['수요 웹툰'] = weddic
    tmp['목요 웹툰'] = thudic
    tmp['금요 웹툰'] = fridic
    tmp['토요 웹툰'] = satdic
    tmp['일요 웹툰'] = sundic
    tmpA = {}
    tmpB = {}
    tmpA['네이버'] = tmp
    tmpB['웹툰'] = tmpA
    return tmpB
    """
    json_val = json.dumps(tmpA, ensure_ascii=False)
    return json_val
    """

def post_list(request):
    return JsonResponse(get_webtoonlink(), safe=False)
