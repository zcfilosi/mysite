from rest_framework import serializers
from .models import *

class todoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = todoItem
        fields = ('content', 'parent_id', 'description', 'is_checked')
