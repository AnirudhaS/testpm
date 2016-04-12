# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from testpm.permissions import IsAuthenticatedByApp

class TestPM(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = (
      IsAuthenticatedByApp,
    )
    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)

