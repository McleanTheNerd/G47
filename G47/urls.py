"""G47 URL Configuration"""


from django.contrib import admin
from django.urls import path,include
from G47App import views as v
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('cms/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',login_required(v.blacksite))
]
