from rest_framework import serializers
from themagicai.app.models import Letter, PostCV
from themagicai.app.serializers import SkillSerializer


class LetterSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(read_only=True, many=True)

    class Meta:
        model = Letter
        exclude = ['result', 'user', 'about', 'requirement']


class LetterDetailSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(read_only=True, many=True)

    class Meta:
        model = Letter
        exclude = ['user']


class PostCVSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(read_only=True, many=True)

    class Meta:
        model = PostCV
        exclude = ['result', 'user', 'about', 'requirement']


class PostCVDetailSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(read_only=True, many=True)

    class Meta:
        model = PostCV
        exclude = ['user']
