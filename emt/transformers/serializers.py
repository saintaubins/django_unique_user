from rest_framework import serializers
from transformers.models import Transformer
from django.contrib.auth.models import User
  
class TransformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transformer
        fields = "__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User