from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'article',)
        read_only_fields = ('article',)


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(          # 이름 바꾸면 안됨
        many=True,
        read_only=True
    )
    comment_count = serializers.IntegerField( # 이름 바꿔도 됨. 사용자 정의 field
        source='comment_set.count',
        read_only=True
    )
    class Meta:
        model = Article
        # fields = '__all__'
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comment_set', 'comment_count',)
        # read_only_fields = ('comment_set', 'comment_count',)
