"""kidney_fond URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from webapp.views import IndexView, AboutUsView, ContactView, KidneyDiseaseIsView, DoctorView, KidneyDiseaseDetailView, \
    IndexBlogView, ForPatientsView, AdviceDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('blog/<int:pk>/', IndexBlogView.as_view(), name='blog'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('kidney_disease_is/', KidneyDiseaseIsView.as_view(), name='kidney_disease_is'),
    path('kidney_disease_is/<int:pk>/', KidneyDiseaseDetailView.as_view(), name='kidney_disease_detail'),
    path('advice_detail/<int:pk>/', AdviceDetailView.as_view(), name='advice_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('doctors/', DoctorView.as_view(), name='doctors'),
    path('for_patients/', ForPatientsView.as_view(), name='for_patients'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
