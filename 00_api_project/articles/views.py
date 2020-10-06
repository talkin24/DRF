from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.core import serializers
from django.http.response import JsonResponse

from articles.serializers import ArticleSerializer

from .models import Article


def article_list_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article_list_html.html', context)


def article_list_json_1(request):
    articles = Article.objects.all()
    articles_json = []
    # article = Article.objects.get(pk=1)
    # test = {
    #     'id': article.id,
    #     'title': article.title,
    #     'content': article.content,
    #     'created_at': article.created_at,
    #     'updated_at': article.updated_at,
    # }
    for article in articles:
        articles_json.append({
            'id': article.id,
            'title': article.title,
            'content': article.content,
            'created_at': article.created_at,
            'updated_at': article.updated_at,
        })
    return JsonResponse(test)


def article_list_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize("json", articles)
    # print(data)
    # print(type(data))
    return HttpResponse(data, content_type='application/json')
    

@api_view(['GET'])
def article_list_json_3(request):
    article = Article.objects.get(pk=1)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)