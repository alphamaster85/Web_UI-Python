"""form_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from formapp import views
from authapp.views import login
# from authapp.views import logout

urlpatterns = [
    path('/admin/logout/', login.index, name='home'),
    path('admin/', admin.site.urls),
    path('form/1', admin.site.urls),
    path('form/<int:user_id>', views.formapp),
    path('', login.index, name='home'),
    path('admin/', admin.site.urls),

]
