import requests
from bs4 import BeautifulSoup

"""
장고에 등록된 모델이나 함수를 사용하여 에러 발생으로 인한 임포트🚨
"""
import os
import django
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
# 모델 불러오기
from books.models import Book

# ============베이스 코드============
api_key = os.getenv("API_KEY")
isbn = "&isbn13=" + "9788983921987"
format = "&format=" + "xml"

# ============도서관 코드============
# libCode = "&libCode=" + "111314"
# type = "&type=" + "ALL"
# pageNo = "&pageNo=" + "1"
# pageSize = "&pageSize=" + "1"


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
like_pageNo = "&pageNo=" + "6"
like_pageSize = "&pageSize=" + "500"


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
        _publication_year = soup.find("publication_year").get_text()
        _class_nm = soup.find("class_nm").get_text()
        _bookImageURL = soup.find("bookImageURL").get_text()
        _description = soup.find("description").get_text()

        # 불필요한 문자 공백으로 치환
        _authors = _authors.replace(";", " | ")
        _authors = _authors.replace(" ;", " | ")
        _description = _description.replace("&lt;", "")
        _description = _description.replace("&gt;", "")

        # 북커버가 있고 알라딘(화질 좋은) 이미지일 경우에만 패스
        thumb = "bookthumb"
        if _bookImageURL:
            if thumb in _bookImageURL:
                continue
        else:
            continue

        # 책 제거
        if _bookname.startswith("("):
            continue

        if "7년의" in _bookname or "아홉살" in _bookname or "몽실" in _bookname:
            continue

        if "아몬드" in _bookname:
            _bookname = "아몬드"

        # 책 제목 특정 문자를 기준으로 슬라이싱
        try:
            colon = _bookname.index(":")
            _bookname = _bookname[:colon]
        except:
            pass
        try:
            same = _bookname.index("=")
            _bookname = _bookname[:same]
        except:
            pass
        try:
            dot = _bookname.index(".")
            _bookname = _bookname[:dot]
        except:
            pass

        """
        # 출판년도를 최신 것으로만 패스
        # _space = ""
        # if _publication_year is not _space:
        #     if int(_publication_year) >= 2016:
        #         pass
        #     else:
        #         continue
        # else:
        #     continue
        """

        """
        import cv2
        import numpy as np

        # 이미지 해상도 높이기
        # _bookImageURL = f'"{_bookImageURL}"'
        sr = cv2.dnn_superres.DnnSuperResImpl_create()
        print(_bookImageURL)
        image = cv2.imread(_bookImageURL)
        print(image)
        # path = "models/EDSR_3.pb"
        # sr.readModel(path)
        # sr.setModel("edsr", 3)

        # # 커널 생성(대상이 있는 픽셀을 강조)
        # kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        # # 커널 적용
        # image_sharp = cv2.filter2D(image, -1, kernel)
        _bookcover = sr.upsample(image)
        """

        """
        from PIL import Image, ImageEnhance

        enhancer = ImageEnhance.Sharpness(_bookImageURL)
        _bookcover = enhancer.enhance(2.0).save()
        """

        # 모델에 입력
        book = Book(
            bookname=_bookname,
            authors=_authors,
            publisher=_publisher,
            publication_year=_publication_year,
            class_nm=_class_nm,
            bookcover=_bookImageURL,
            description=_description,
        )
        book.save()


book_info()
