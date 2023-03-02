from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Author
from .serializers import AuthorSerializer


class AuthorListCreateAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
