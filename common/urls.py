from django.urls import path
from common.views import *

urlpatterns = [
    path('', home_page_view, name='home'),
]