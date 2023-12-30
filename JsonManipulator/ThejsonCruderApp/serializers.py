from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    user_name = serializers.CharField()
    email_id = serializers.CharField()
    