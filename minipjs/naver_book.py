import os
import sys
import urllib.request
import json
import pandas as pd
from .naver_key import *

def naver_book_search(keyword):

    page = 1
    start_num = 1
    n_item = 100
    books_list = []
    # global c_id
    # global c_secret
    while True:
        client_id = c_id  # api id
        client_secret = c_secret  # api password
        encText = urllib.parse.quote(keyword)   # 검색어
        url = "https://openapi.naver.com/v1/search/book.json?query=" + encText # url 주소
        url += f"&display={n_item}&start={start_num}&sort=sim" # 1페이지에 출력할 결과 수(n_item), 결과 시작 번호(page)
        print(url)
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)  # url, id, pw 를 종합해서 서버에 결과 요청
        rescode = response.getcode() # 서버 응답 코드 받기
        if(rescode==200):
            response_body = response.read()
        #     print(response_body.decode('utf-8'))
        else:
            print("Error Code:" + rescode)
        data = response_body.decode('utf-8')
        data = json.loads(data)
        total_page = data['total'] // n_item + 1  # 923 // 100 = 9, 23    , total_page: 10
        books_list.append(data)

        if page == total_page:
            break

        page += 1
        start_num += 100
    books = []
    for i in books_list: # 100개씩 수집된 자료를 i에 저장
        for j in i['items']:   # items에 있는 100개의 자료를 j에 한개 씩 꺼내 담음
            books.append(j.values())  # .values()로 j에 있는 책 정보 값을 모두 꺼내서 books에 append

    df = pd.DataFrame(books, columns=data['items'][0].keys())
    
    return df

