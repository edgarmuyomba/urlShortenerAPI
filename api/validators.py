from rest_framework import serializers
from .models import *
import re

def uniqueSourceValidator(value):
    domain = getDomain(value)
    if Url.objects.filter(source__icontains=domain).exists():
        raise serializers.ValidationError("A url with this domain already exists")
    return value 

def getDomain(value):
    regex = r'^(?:https?:\/\/)?(?:www\d?\.)?(?P<domain>[\w.-]+)(?:\.\w+)+(?:\/|$)'
    match = re.match(regex, value)
    try:
        domain = match.group('domain')
    except AttributeError:
        domain = None 
    return domain