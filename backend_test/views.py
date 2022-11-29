from django.shortcuts import render
import urllib.request
import json

# Create your views here.
def index(request):
    if request.method == 'GET':

        client_id = "Jl5rK_P9cdCDLGlhIPuy"
        client_secret = "7DZU261Y4v"
        q = request.GET.get('q')
        encText = urllib.parse.quote("{}".format(q))
        url = "https://openapi.naver.com/v1/search/book.json?query=" + encText # JSON 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
        api_request = urllib.request.Request(url)
        api_request.add_header("X-Naver-Client-Id",client_id)
        api_request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(api_request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')


    context = {
                'items' : items
            }

    return render(request, 'checkup/index.html', context=context)