from django.shortcuts import render
import urllib.request
import json
from django.db.models import Q
from books.models import Book
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

    return render(request, 'backend_test/index.html', context=context)
    
def search(request):
    books = Book.objects.get(pk=1)
    book = None
    query = None
    if "search" in request.GET:
        query = request.GET.get("search")
        book = Book.objects.order_by("-pk").filter(
            Q(bookname__contains=query) | Q(authors__contains=query)
        )
    context = {
        "query": query,
        "book": book,
        "books" : books
    }
    return render(request, 'backend_test/index.html', context)

def map(request):
    return render(request, "backend_test/map.html")

def map2(request):
    return render(request, "backend_test/map2.html")

