from django.shortcuts import render
from django.views import View

from webapp.models import Doctor, Patient, AboutUs, AboutRead, Image, AboutUsImage, IndexBlog, Advices, ForPatientBlog


class IndexView(View):
    def get(self, request, *args, **kwargs):
        doctors = IndexBlog.objects.all()[:4]
        patients = Patient.objects.all()
        image = Image.objects.last()
        return render(request, 'index.html', context={'doctors': doctors, 'patients': patients, 'image': image})


class IndexBlogView(View):
    def get(self, request, pk, *args, **kwargs):
        blog = IndexBlog.objects.get(pk=pk)
        return render(request, 'article.html', context={'blog': blog})


class AboutUsView(View):
    def get(self, request):
        about = AboutUsImage.objects.last()
        doctors = Doctor.objects.all()
        about_list = AboutUs.objects.all()
        return render(request, 'about.html', context={'about': about, 'doctors': doctors, 'about_list': about_list})


class KidneyDiseaseIsView(View):
    def get(self, request):
        about_read = AboutRead.objects.all()
        return render(request, 'services.html', context={'about_read': about_read})


class KidneyDiseaseDetailView(View):
    def get(self, request, pk):
        about_read_detail = AboutRead.objects.get(pk=pk)
        return render(request, 'disease_detail.html', context={'about_read_detail': about_read_detail})


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html')


class DoctorView(View):
    def get(self, request):
        doctors_first_level = Doctor.objects.all()[:4]
        doctors_second_level = Doctor.objects.all()[4:]
        return render(request, 'location.html', context={'doctors': doctors_first_level,
                                                         'doctors_second_level':doctors_second_level,})


class ForPatientsView(View):
    def get(self, request, *args, **kwargs):
        about_read = Patient.objects.all()
        blogs = ForPatientBlog.objects.all()
        return render(request, 'for_patients.html', context={'about_read': about_read, 'blogs': blogs})


class AdviceDetailView(View):
    def get(self, request, pk):
        advice = Advices.objects.get(pk=pk)
        return render(request, 'advice.html', context={'advice': advice})