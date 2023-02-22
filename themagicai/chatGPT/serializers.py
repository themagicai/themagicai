from rest_framework import serializers
from themagicai.app.models import Letter, PostCV


class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        exclude = ['result']


class PostCVSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCV
        exclude = ['result']
