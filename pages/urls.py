from django.urls import path

from .views import *

app_name = "pages"
urlpatterns = [
    # Home...
    path('', HomePageView.as_view(), name='home'),

    # About...
    path('about/', AboutPageView.as_view(), name='about'),

    # Services...
    path('services/', ServicesPageView.as_view(), name='services'),

    # Contact...
    path('contact/', ContactPageView.as_view(), name='contact'),

]
