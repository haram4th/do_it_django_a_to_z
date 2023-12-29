import pandas as pd
import numpy as np
from .dbinfo import *
import joblib
import os
from .models import Yes24Bestlist

# DB에서 yes24best 중복 제거한 전체 데이터 받아오기
# def book_detail(dbid, dbpw, table_name):
# from sqlalchemy import create_engine
# import pymysql
# pymysql.install_as_MySQLdb()

# engine = create_engine(f"mysql+mysqldb://{dbid}:{dbpw}@{dbaddr}:{dbpt}/{dbname}")
# conn = engine.connect()
# book = pd.DataFrame()
# try:
#     book = pd.read_sql(f"SELECT * FROM yes24_book_detail", con=conn)
#     print("DB Loading Success", end="\r")
# except Exception as e:
#     print(e)
#     conn.close()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
img_dir = os.path.join(BASE_DIR, '_static', 'yes24', 'recommand')
# similarities를 파일에서 불러오기
file_path = os.path.join(img_dir, 'yes24_recom_list.joblib')
similarities = joblib.load(file_path)

# 추천함수 정의
def get_recommendations(book_id):
    try:
        book_title = Yes24Bestlist.objects.filter(book_id=book_id).values_list('title_m', flat=True).get() # - 1
        similar_books = similarities[book_title]
        print(similar_books.items())
        similar_books = similar_books.keys()
        
        return similar_books
    except Yes24Bestlist.DoesNotExist:
        # 예외 처리: 해당 book_id에 해당하는 레코드가 없을 경우
        return None

