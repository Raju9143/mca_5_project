from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('dadmin/', admin.site.urls),
    path('admin/',include('admin.urls')),
    path('',include('user.urls')),
]
