from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "accounts/index.html")

# 네이버 api를 사용한 검색기능입니다. 필요 없어질시 삭제 하셔도 됩니다.
# def naver(request):
#     if request.method == 'GET':

#         client_id = "client_id"
#         client_secret = "client_secret"
#         q = request.GET.get('q')
#         encText = urllib.parse.quote("{}".format(q))
#         url = "https://openapi.naver.com/v1/search/book.json?query=" + encText # JSON 결과
#         # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
#         api_request = urllib.request.Request(url)
#         api_request.add_header("X-Naver-Client-Id",client_id)
#         api_request.add_header("X-Naver-Client-Secret",client_secret)
#         response = urllib.request.urlopen(api_request)
#         rescode = response.getcode()
#         if(rescode==200):
#             response_body = response.read()
#             result = json.loads(response_body.decode('utf-8'))
#             items = result.get('items')


#     context = {
#                 'items' : items
#             }

#     return render(request, 'checkup/naver.html', context=context)