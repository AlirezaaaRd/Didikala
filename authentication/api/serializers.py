from rest_framework import serializers
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Userseralizers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


