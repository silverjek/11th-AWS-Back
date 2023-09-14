from rest_framework import serializers
from .models import *

class PostSerializer(serializers.Model):
    class Meta:
        model = Post
        fields = '__all__'