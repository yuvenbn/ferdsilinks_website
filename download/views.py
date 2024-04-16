import os
from django.http import FileResponse, HttpResponse
from django.views import View
from django.conf import settings
# Create your views here.

class DownloadZipView(View):
    def get(self, request):
        zip_file_path = 'static/downloads/startup-website-template.zip'
        if os.path.exists(zip_file_path):
            return FileResponse(open(zip_file_path, 'rb'), as_attachment=True)
        else:
            return HttpResponse('File Not Found')