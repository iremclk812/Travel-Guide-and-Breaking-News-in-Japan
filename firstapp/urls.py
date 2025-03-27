from django.urls import path


from . import views


urlpatterns = [
     path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name="contact"),
    path('news/',views.news,name='news'),
    path('destinations/',views.destination_list,name="destination-list"),
    path('destinations/new/',views.create_destination ,name='destination-create'),
path('destinations/delete/<int:pk>',views.delete_destination,name="destination-delete"),
    path('destinations/<int:pk>/edit',views.edit_destinaton,name="destination-edit"),
    path('news/new/' ,views.create_news,name='news-create'),
    path('news/delete/<int:pk>',views.delete_news,name="news-delete"),
    path('news/<int:pk>/edit',views.edit_news,name="news-edit"),
 ]
