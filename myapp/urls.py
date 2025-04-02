from django.urls import path
from .models import index

urlpatterns = [
    path ('', view.index,'index')
]