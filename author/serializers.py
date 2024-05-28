from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    pseudonym = serializers.CharField(
        max_length=64,
        required=False
    )
    age = serializers.IntegerField(min_value=1)
    retired = serializers.BooleanField()

    class Meta:
        model = Author
        fields = "__all__"
