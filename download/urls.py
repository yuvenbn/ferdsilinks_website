

from django.urls import path
from .views import *

app_name = "download"
urlpatterns = [
    # Download...
    path('products/solafide-accounting', DownloadZipView.as_view(), name='solafide-accounting-download'),
]
