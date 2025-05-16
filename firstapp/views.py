from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Destination
from .serializers import DestinationSerializer
from .models import News
from .serializers import NewsSerializer
from rest_framework import status
from django.shortcuts import render
from .models import Destination, News
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view


def index(request):
    destinations = Destination.objects.all()  # Tüm destinasyonları alın
    return render(request, 'index.html', {'destinations': destinations})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def news(request):
    news = News.objects.all()  # Tüm haberleri alın
    return render(request, 'news.html', {'news': news})


@api_view(['GET', 'POST'])
def destination_list(request):
    if request.method == 'GET':
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True
                                           )
        return Response(serializer.data)

    elif request.method == 'POST':

        destination_id = request.data.get('id', None)

        if destination_id:
            try:
                destination = Destination.objects.get(id=destination_id)
            except Destination.DoesNotExist:
                return Response({"error": "Destination not found."}, status=status.HTTP_404_NOT_FOUND)

            serializer = DestinationSerializer(destination, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Destination updated successfully.",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            serializer = DestinationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Destination created successfully.",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def news_list(request):
    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        news_id = request.data.get('id', None)

        if news_id:
            try:
                news_item = News.objects.get(id=news_id)
            except News.DoesNotExist:
                return Response({"error": "News not found."}, status=status.HTTP_404_NOT_FOUND)

            serializer = NewsSerializer(news_item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "News updated successfully.",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:  # Yeni kayıt oluşturma
            serializer = NewsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "News created successfully.",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'POST'])
def delete_destination(request, pk):
    destination = get_object_or_404(Destination, id=pk)
    if destination:
        if request.method == 'DELETE' or request.method == 'POST':
            destination.delete()
            return Response({"message": f"Destination with id {pk} has been deleted successfully."},
                            status=status.HTTP_200_OK)
    else:
        return Response({"message": f"Destination with id {pk} not found."},
                        status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE', 'POST'])
def delete_news(request, pk):
    news_item = get_object_or_404(News, id=pk)
    if request.method == 'DELETE' or request.method == 'POST':
        news_item.delete()
        return Response({"message": f"News with id {pk} has been deleted successfully."},
                        status=status.HTTP_204_NO_CONTENT)

    # GET methodu için bir yanıt döner
    return Response({
        "message": "This endpoint is for deleting news. Please use DELETE method to delete the resource."
    }, status=status.HTTP_200_OK)
