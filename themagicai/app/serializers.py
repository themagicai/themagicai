from rest_framework import serializers
from themagicai.app.models import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ['is_active']
