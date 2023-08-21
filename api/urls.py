from django.urls import path 
from .views import *

app_name = 'api'

urlpatterns = [
    path('', getLink, name="get_link"),
    path('<int:pk>/', urlMap, name="redirect")
]