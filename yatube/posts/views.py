from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HTTPResponse('Главная страница')


# def group_posts(request, pk):
#     return HTTPResponse(f'группа {pk}')
