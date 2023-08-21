from rest_framework import serializers
from .models import * 
from .validators import uniqueSourceValidator

class URLSerializer(serializers.ModelSerializer):
    source = serializers.URLField(validators=[uniqueSourceValidator])
    class Meta:
        model = Url
        fields = '__all__'