from django.urls import path

from author.views import (AuthorListCreateAPIView,
                          AuthorRetrieveUpdateDestroyAPIView)


app_name = "author"

urlpatterns = [
    path("", AuthorListCreateAPIView.as_view(), name="list-create-author"),
    path("<int:pk>/", AuthorRetrieveUpdateDestroyAPIView.as_view(), name="author-retrieve-update-destroy")
]
