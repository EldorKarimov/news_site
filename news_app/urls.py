from django.urls import path
from .views import home, category_news, city_news, detail_news

urlpatterns = [
    path('', home, name = 'home'),
    path('category_news/<slug:slug>', category_news, name='category_news'),
    path('city_news/<slug:slug>', city_news, name = 'city_news'),
    path('detail_news/<slug:slug>', detail_news, name = 'detail_news'),
]