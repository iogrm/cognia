from rest_framework import serializers


class SingleCharacterSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    cover = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)
    title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=256)
    description = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=2048)
    isFemale = serializers.BooleanField(required=True, allow_null=False)
    mbti = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=64)


class SubmitCharacterSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    cover = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)
    title = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=256)
    description = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=2048)
    mbti = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=64)
    isFemale = serializers.BooleanField(required=True, allow_null=False)
    category_id = serializers.IntegerField(required=True, allow_null=False)


class UpdateCharacterCoverSerializer(serializers.Serializer):
    character_id = serializers.IntegerField(required=True, allow_null=False)
    cover = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)


class DeleteCharacterSerializer(serializers.Serializer):
    character_id = serializers.IntegerField(required=True, allow_null=False)
