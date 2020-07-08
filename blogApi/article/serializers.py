from rest_framework import serializers

from .models import *

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('author_id','title', 'description', 'body', 'id')