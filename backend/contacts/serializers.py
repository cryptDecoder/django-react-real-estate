from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Contacts


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'
