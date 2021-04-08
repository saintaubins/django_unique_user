from rest_framework import serializers
from transformers.models import Transformer, Customer
from django.contrib.auth.models import User
  
class TransformerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transformer
        fields = "__all__"

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"