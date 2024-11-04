# myproject/urls.py

from django.contrib import admin
from django.urls import path
from pfm import views  # Ensure 'yourapp' is replaced with the actual app name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # This should match the view function you created
]
