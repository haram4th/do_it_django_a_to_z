from django.shortcuts import render
from .naver_book import *


def main(request):
    return render(request, "main.html")


def calculator(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        oper = request.POST.get('oper')

        if oper == '+':
            result = num1 + num2
        elif oper == '-':
            result = num1 - num2
        elif oper == '*':
            result = num1 * num2
        elif oper == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Cannot divide by zero'
        else:
            result = 'Invalid operation'

        context = {'result': result, 'num1': num1, 'num2' : num2, 'oper' : oper}

        return render(request, 'calc/calculator.html', context=context)

    return render(request, 'calc/calculator.html')

def naver_book(request):
    if request.method == 'POST':
        keyword = request.POST.get("keyword")
        
        # naver_book_search 함수로 네이버 API 에서 책을 검색하고 
        # 결과로 반환된 데이터프레임을 HTML 테이블로 변환
        book_list = naver_book_search(keyword)
        book_list = book_list.drop(["link", 'image'], axis=1)
        html_table = book_list.to_html(index=True, classes='table table-striped')
        
        # HTML 테이블을 conext에 넣어 템플릿으로 전달
        context = {"keyword" : keyword, 'html_table': html_table}
                
        return render(request, 'naver_book/naver_book.html', context=context)
    
    return render(request, 'naver_book/naver_book.html')
    
