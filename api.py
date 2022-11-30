import requests
from bs4 import BeautifulSoup

"""
장고에 등록된 모델이나 함수를 사용하여 에러 발생으로 인한 임포트🚨
"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# 모델 불러오기
from books.models import Book

# ============베이스 코드============
# 인증키 1: c30a173104dbac8b7924d537a3ec76270dda1187394b8cd8a8f2ae3b1bdd509a
# 인증키 2: 4b79eb502a251ec0b573ee817ed0c953145c242f3f57da8cdb61056c69371b64
api_key = "4b79eb502a251ec0b573ee817ed0c953145c242f3f57da8cdb61056c69371b64"
isbn = "&isbn13=" + "9788983921987"
format = "&format=" + "xml"

# ============도서관 코드============
libCode = "&libCode=" + "111314"
type = "&type=" + "ALL"
pageNo = "&pageNo=" + "1"
pageSize = "&pageSize=" + "1"


"""도서관별 장서/대출 데이터 조회"""
# def library():
#     URL = (
#     "http://data4library.kr/api/itemSrch?authKey="
#     + api_key
#     + libCode
#     + type
#     + pageNo
#     + pageSize
#     + format
#     )

#     # print(URL)
#     response = requests.get(URL)

#     soup = BeautifulSoup(response.text, "xml")
#     bookIds = soup.find_all("isbn13")

#     bookIds_list = []
#     for id in bookIds:
#         bookIds_list.append(id.get_text())

#     return bookIds_list

# library()

# ============인기도서 코드============
like_pageNo = "&pageNo=" + "1"
like_pageSize = "&pageSize=" + "100"


def book_like():
    """인기대출 도서 조회"""

    URL = (
        "http://data4library.kr/api/loanItemSrch?authKey="
        + api_key
        + like_pageNo
        + like_pageSize
        + format
    )
    print(URL)
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, "xml")
    bookIds = soup.find_all("isbn13")

    bookIds_list = []
    for id in bookIds:
        bookIds_list.append(id.get_text())

    return bookIds_list


book_like()


def book_info():
    """. 도서 상세 조회"""
    # for bookId in library():
    for bookId in book_like():

        URL = (
            "http://data4library.kr/api/srchDtlList?authKey="
            + api_key
            + "&isbn13="
            + bookId
            + format
        )
        # print(URL)

        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "xml")

        _bookname = soup.find("bookname").get_text()
        _authors = soup.find("authors").get_text()
        _publisher = soup.find("publisher").get_text()
        year = soup.find("publication_year").get_text()
        _bookImageURL = soup.find("bookImageURL").get_text()
        _description = soup.find("description").get_text()

        if _bookImageURL:
            pass
        else:
            continue

        book = Book(
            bookname=_bookname,
            authors=_authors,
            publisher=_publisher,
            publication_year=year,
            bookcover=_bookImageURL,
            description=_description,
        )
        book.save()


book_info()
