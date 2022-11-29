import requests
import json
from bs4 import BeautifulSoup

api_key = ""
isbn = "&isbn13=" + "9788983921987"
format = "&format=" + "xml"


# ===================
libCode = "&libCode=" + "141321"
type = "&type=" + "ALL"
pageNo = "&pageNo=" + "1"
pageSize = "&pageSize=" + "100"

def library():
    URL = (
    "http://data4library.kr/api/itemSrch?authKey=" 
    + api_key 
    + libCode 
    + type
    + pageNo
    + pageSize
    + format
    )
    
    # print(URL)
    response = requests.get(URL)
    
    soup = BeautifulSoup(response.text, "xml")
    bookIds = soup.find_all("isbn13")

    bookIds_list = []
    for id in bookIds:
        bookIds_list.append(id.get_text())
    
    return bookIds_list

library()


def book_info():
    for bookId in library():
    
        URL = (
        "http://data4library.kr/api/srchDtlList?authKey=" 
        + api_key 
        + "&isbn13=" + bookId
        + format
        )
        print(URL)

        response = requests.get(URL)

        soup = BeautifulSoup(response.text, "xml")
        _no = soup.find("no").get_text()
        _bookname = soup.find("bookname").get_text()
        _authors = soup.find("authors").get_text()
        _publisher = soup.find("publisher").get_text()
        _class_no = soup.find("class_no").get_text()
        _class_nm = soup.find("class_nm").get_text()
        _publication_year = soup.find("publication_year").get_text()
        _publication_date = soup.find("publication_date").get_text()
        _bookImageURL = soup.find("bookImageURL").get_text()
        _description = soup.find("description").get_text()

        print(_no)
        print(_bookname)
        print(_authors)
        print(_publisher)
        print(_class_no)
        print(_class_nm)
        print(_publication_year)
        print(_publication_date)
        print(_bookImageURL)
        print(_description)

        # import model
        # book = model(
        #     no = _no,
        #     bookname = _bookname,
        #     authors = _authors,
        #     publisher = _publisher,
        #     class_no = _class_no,
        #     class_nm = _class_nm,
        #     publication_year = _publication_year,
        #     publication_date = _publication_date,
        #     bookImage = _bookImageURL,
        #     description = _description,
        # )
        # book.save()

book_info()