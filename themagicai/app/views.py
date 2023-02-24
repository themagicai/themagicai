from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from themagicai.app.models import Skill
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from themagicai.app.serializers import SkillSerializer


@extend_schema_view(
    list=extend_schema(parameters=[OpenApiParameter(name='q', description="q is required in params")]))
class SkillAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)

    def list(self, request, *args, **kwargs):
        search = request.query_params.get('q')
        if search is None:
            return Response({'error': "You have to send q in params"}, status=status.HTTP_400_BAD_REQUEST)
        queryset = self.get_queryset().filter(name__icontains=search)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
