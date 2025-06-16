"""
URL configuration for selfdjangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from member import views
from blogs import views as blogviews 
from course import views as courseviews 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='Homepage'), 
    path('add-client/', views.add_client, name='add_client'),
    path('client/<int:client_id>/', views.view_client, name='view_client'),
    path('clients/', views.viewclients, name='viewclients'),
    path('api/client/<int:client_id>/', views.api_client_detail, name='api_client_detail'),
    path('blogs/', blogviews.all_blogs, name='all_blogs'),
    path('blog/<slug:slug>/', blogviews.blog_detail, name='blog_detail'),
    path('courses/', courseviews.view_courses, name='view_courses'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
