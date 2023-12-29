from django.shortcuts import render
import os
from glob import glob
import random
from django.conf import settings
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Yes24Bestlist
import re
from .book_recommand import *

pattern = re.compile(r'\d+')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
img_dir = os.path.join(BASE_DIR, '_static', 'yes24')

def yes24index(request):
    
    # glob을 사용하여 jpg 파일을 모두 가져옴
    book_cover_list = glob(os.path.join(img_dir, 'book_img/*.jpg'))
    # list로 변환
    book_cover_list = list(book_cover_list)
    # print(book_cover_list)
    covers_10 = []
    
    for i in range(10):
        num = random.randrange(len(book_cover_list))
        img_url = book_cover_list[num].split("/")[-1]
        img_no = re.findall(pattern, img_url)
        print(img_no[0])
        covers_10.append((img_url, img_no[0]))
    
    print(covers_10)
    context = {'covers_10' : covers_10, }
    
    return render(request, 'yes24/yes24index.html', context)

class BestDetailView(DetailView):
    model = Yes24Bestlist
    template_name = 'yes24/book_detail.html'  # 템플릿 파일의 경로
    context_object_name = 'book'
    pk_url_kwarg = 'book_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cover_name'] = self.request.GET.get('cover_name', '')
        
        input_book_id = self.kwargs.get(self.pk_url_kwarg)
        recommendations = get_recommendations(input_book_id)
        context['recommendations'] = recommendations

        print(f"입력한 도서 '{input_book_id}'와 유사한 도서 {len(recommendations)}개:")
        for i, book_title in enumerate(recommendations):
            print(f"{i + 1}. {book_title}")

        return context

      

