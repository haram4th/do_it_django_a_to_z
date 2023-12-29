from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'minipjs'

urlpatterns = [
    # path('', views.main, name='main'),
    path('', TemplateView.as_view(template_name='main.html'), name='main'),
    path('calculator', views.calculator, name='calculator'),
    path('naver_book', views.naver_book, name='naver_book'),
]

