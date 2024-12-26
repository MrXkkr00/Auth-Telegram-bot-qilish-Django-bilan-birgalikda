from rest_framework import serializers

class GetAuthOTPcode(serializers.Serializer):
    code = serializers.IntegerField(required=True)
