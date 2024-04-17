import os
from django.http import FileResponse, HttpResponse
from django.views import View
from django.conf import settings
# Create your views here.

from django.views.generic import TemplateView
from blog.views import BlogQuerysetMixin

from .models import Download


class DownloadZipView(View):
    def post(self, request):
        if request.method == 'POST':
            data = request.POST
            # Create a download instance
            new_download = Download.objects.create(
                user_fullname = data['user_fullname'],
                email = data['email'],
                country = data['country'],
                file_name = 'Solafide Accounting',
            )

            # Download the Zip file...
            zip_file_path = 'static/downloads/startup-website-template.zip'
            # zip_file_path = '/usr/local/lsws/Example/ferdsilinks_website/ferdsilinks_website/static/downloads/startup-website-template.zip'
            if os.path.exists(zip_file_path):
                return FileResponse(open(zip_file_path, 'rb'), as_attachment=True)
            else:
                return HttpResponse('File Not Found')
        else:
            return HttpResponse('Unauthorized!')