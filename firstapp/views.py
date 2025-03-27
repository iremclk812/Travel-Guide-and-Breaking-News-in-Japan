from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import DestinationForm, NewsForm
from .models import Destination
from .models import News# Modeli kullanacağımız için import edin


# Create your views here.
def index(request):
    destinations = Destination.objects.all()
    return render(request, "index.html", {'destinations': destinations})

def news(request):
    news = News.objects.all()
    return render(request, "news.html", {'news': news})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def destination_list(request):
    destinations = Destination.objects.all()  # Tüm kayıtları al
    return render(request, 'destination_list.html', {'destinations': destinations})

def news_list(request):
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})

def create_destination(request):

    if request.method == "POST":
        form = DestinationForm(request.POST)
        if form.is_valid():
            form.save()  # Kaydı veritabanına kaydet
            return redirect("destination-list")  # Kayıt sonrası listeleme sayfasına yönlendir
    else:
        form = DestinationForm()
    return render(request, 'destination_form.html', {'form': form})

def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news")
    else:  # GET isteği geldiğinde bu kısım çalıştırılacak
        form = NewsForm()
    return render(request, 'news_form.html', {'form': form})



def delete_destination(request, pk):
    destination = get_object_or_404(Destination, pk=pk)  # Kayıt yoksa 404 hatası döndür
    destination.delete()  # Kayıdı sil
    return redirect("destination-list")  # Silme sonrası listeleme sayfasına yönlendir

def delete_news(request,pk):
    news = get_object_or_404(News,pk=pk)
    news.delete()
    return redirect("news")

def edit_destinaton(request,pk):
  destination = get_object_or_404(Destination,pk=pk)
  if request.method == "POST":
    form = DestinationForm(request.POST,instance=destination)
    if form.is_valid():
      form.save()
      return redirect("destination-list")
  else:
    form = DestinationForm(instance=destination)
  return render(request,"destination_form.html",{"form":form})

def edit_news(request,pk):
    news = get_object_or_404(News,pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST,instance=news)
        if form.is_valid():
            form.save()
            return redirect("news")
        else:
            form = NewsForm(instance=news)
            return render(request, 'news_form.html', {'form': form})
