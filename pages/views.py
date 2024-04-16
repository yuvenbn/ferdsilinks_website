from django.views.generic import TemplateView
from blog.views import BlogQuerysetMixin

class HomePageView(BlogQuerysetMixin, TemplateView):
    template_name = "pages/home.html"
    extra_context = {
        'page_title': 'Home',
        'active_links': 'home'
    }

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
    extra_context = {
            'page_title': 'About Us',
            'active_links': 'about'
        }

class ServicesPageView(TemplateView):
    template_name = "pages/services.html"
    extra_context = {
            'page_title': 'Services',
            'active_links': 'services'
        }

class ContactPageView(TemplateView):
    template_name = "pages/contact.html"
    extra_context = {
            'page_title': 'Contact',
            'active_links': 'contact'
        }
