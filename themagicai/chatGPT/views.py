import openai
from rest_framework.response import Response
from rest_framework import viewsets
from themagicai.app.models import Letter, PostCV
from rest_framework import status
from themagicai.chatGPT.serializers import LetterSerializer, PostCVSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

openai.api_key = "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"


def openai(req):
    # req = f"{title}\n\nJob: {job}\nCompany: {company}\n{body}\nMy CV:{cv}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=req,
        max_tokens=3
    )
    return response


class PostCVAPIView(viewsets.ModelViewSet):
    queryset = PostCV.objects.all()
    serializer_class = PostCVSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        letters = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(letters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class LetterAPIView(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        letters = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(letters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
