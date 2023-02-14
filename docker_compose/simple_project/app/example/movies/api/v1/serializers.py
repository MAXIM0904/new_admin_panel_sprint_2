from rest_framework import serializers


class FilmWorkSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    creation_date = serializers.DateTimeField(read_only=True)
    rating = serializers.FloatField()
    type = serializers.CharField(max_length=255, read_only=True)
    genres = serializers.ListField()
    actors = serializers.ListField()
    directors = serializers.ListField()
    writers = serializers.ListField()

