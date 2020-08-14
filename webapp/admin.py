from django.contrib import admin
from image_cropping import ImageCroppingMixin

from webapp.models import Doctor, Patient, AboutUs, AboutRead, Image, AboutUsImage, IndexBlog, Advices, ForPatientBlog


class DoctorAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['name', 'portfolio']


class PatientAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['name', 'portfolio']


class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['image']


class AboutUsImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['image']


class AboutUsAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['text1', 'text2']


class AboutReadAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['title', 'text']


class AdvicesAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['title', 'text']


class IndexBlogAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['title', 'text']


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, DoctorAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(AboutRead, AboutReadAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(AboutUsImage, AboutUsImageAdmin)
admin.site.register(IndexBlog, IndexBlogAdmin)
admin.site.register(Advices, AdvicesAdmin)
admin.site.register(ForPatientBlog)
