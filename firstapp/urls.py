from django.urls import path

from . import views
from .views import destination_list, news_list, delete_destination, delete_news

urlpatterns = [
   path('', views.index, name='index'),  # Ana sayfa
    path('about/', views.about, name='about'),  # Hakkında
    path('contact/', views.contact, name="contact"),  # İletişim
    path('news/', views.news, name='news'),

    path('api/destinations/', destination_list, name='destination-list'),
    path('api/news/', news_list, name='news-list'),
    path('api/destinations/<int:pk>/delete/', delete_destination, name='delete-destination'),
    path('api/news/<int:pk>/delete/', delete_news, name='delete-news'),

]
