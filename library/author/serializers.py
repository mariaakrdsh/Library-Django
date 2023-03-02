from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "name", "surname", "patronymic", "books")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(instance.books)
        representation["books"] = {
            "name": instance.books.name
        }
        return representation
