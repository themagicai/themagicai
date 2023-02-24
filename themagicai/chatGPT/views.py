import openai
from openai.error import AuthenticationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from config.settings.base import env
from themagicai.app.models import Letter, PostCV
from rest_framework import status
from themagicai.app.serializers import SkillSerializer
from themagicai.chatGPT.serializers import LetterSerializer, PostCVSerializer, PostCVDetailSerializer, \
    LetterDetailSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.contrib.auth import get_user_model

User = get_user_model()


def request_to_chatGPT(name, company, position, requirement, skills, about, type):
    if type not in ['letter', 'CV']:
        return {'error': True}

    if type == 'CV':
        token = 600
        req = f"Write me a CV for the job below based on my experience in Resume below\n\nFullname: {name}\n\nPosition: {position}\nCompany: {company}\n Requirement: {requirement}\nSkills:{skills}\nAbout: {about}"
    elif type == 'letter':
        token = 350
        req = f"Write me a cover letter for the vacancy below on my experience\n\nFullname: {name}\n\nPosition: {position}\nCompany: {company}\n Requirement: {requirement}\nSkills:{skills}\nAbout: {about}"

    openai.api_key = env("CHAT_GPT_SECRET_KEY")
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=req,
            max_tokens=5
        )
    except AuthenticationError:
        return {"error": True}
    return response


class PostCVAPIView(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.ListModelMixin, GenericViewSet):
    queryset = PostCV.objects.all()
    serializer_class = PostCVSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        letters = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(letters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        check = self.check_attempts(request)
        if check.get("error"):
            return Response({"error": True, "message": "You don't have attempts"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        obj = self.get_queryset().get(id=serializer.data.get('id'))
        skills = obj.skills.all().values_list('name', flat=True)
        res = ','.join(skills)
        response = request_to_chatGPT(request.user.name, serializer.data.get('company'),
                                      serializer.data.get('position'),
                                      serializer.data.get('requirement'),
                                      res, serializer.data.get('about'), 'CV')
        if response.get('error'):
            return Response({"message": "There was an error, please connect with admin"},
                            status=status.HTTP_400_BAD_REQUEST)

        obj.result = response.choices[0].text
        obj.save()
        return Response({"result": response.choices[0].text}, status=status.HTTP_200_OK)

    def check_attempts(self, request):
        att = self.get_queryset().filter(user=request.user).count()
        if att >= 2:
            return {'error': True}
        return {'error': False}


class PostCVDetailAPIView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = PostCV.objects.all()
    serializer_class = PostCVDetailSerializer
    permission_classes = [IsAuthenticated]


class LetterAPIView(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.ListModelMixin, GenericViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        letters = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(letters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        check = self.check_attempts(request)
        if check.get("error"):
            return Response({"error": True, "message": "You don't have attempts"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        obj = self.get_queryset().get(id=serializer.data.get('id'))
        skills = obj.skills.all().values_list('name', flat=True)
        res = ','.join(skills)
        response = request_to_chatGPT(request.user.name, serializer.data.get('company'),
                                      serializer.data.get('position'),
                                      serializer.data.get('requirement'),
                                      res, serializer.data.get('about'), 'letter')
        if response.get('error'):
            return Response({"message": "There was an error, please connect with admin"},
                            status=status.HTTP_400_BAD_REQUEST)
        obj.result = response.choices[0].text
        obj.save()
        return Response({"result": response.choices[0].text}, status=status.HTTP_200_OK)

    def check_attempts(self, request):
        att = self.get_queryset().filter(user=request.user).count()
        if att >= 2:
            return {'error': True}
        return {'error': False}


class LetterDetailAPIView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterDetailSerializer
    permission_classes = [IsAuthenticated]
