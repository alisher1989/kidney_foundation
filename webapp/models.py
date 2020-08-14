from django.db import models
from image_cropping import ImageRatioField


class Doctor(models.Model):
    name = models.CharField('Name', max_length=250, null=True, blank=True)
    image = models.ImageField('Photo', upload_to='media/', null=True, blank=True)
    cropping = ImageRatioField('image', '430x500')
    portfolio = models.TextField('Портфолио', max_length=2000, null=True, blank=True)


class Patient(models.Model):
    name = models.CharField('Name', max_length=250, null=True, blank=True)
    image = models.ImageField('Photo', upload_to='media/', null=True, blank=True)
    cropping = ImageRatioField('image', '430x500')
    portfolio = models.TextField('Portfolio', max_length=2000, null=True, blank=True)


class AboutUs(models.Model):
    text1 = models.TextField('First text', max_length=2000, null=True, blank=True)
    text2 = models.TextField('Second text', max_length=2000, null=True, blank=True)
    image = models.ImageField('Image', upload_to='media/', null=True, blank=True)
    cropping = ImageRatioField('image', '669x300')


class AboutUsImage(models.Model):
    image = models.ImageField('Image', upload_to='media/', null=True, blank=True)
    cropping = ImageRatioField('image', '677x218')


class AboutRead(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    text = models.TextField(max_length=10000, null=True, blank=True)
    image = models.ImageField('Image', upload_to='media/', null=True, blank=True)
    cropping = ImageRatioField('image', '900x300')


class Image(models.Model):
    image = models.ImageField('Image', upload_to='media/', null=True, blank=True)
    cropping = ImageRatioField('image', '460x220')


class IndexBlog(models.Model):
    title = models.TextField('Title', max_length=2000, null=True, blank=True)
    title2 = models.TextField('Title2', max_length=2000, null=True, blank=True)
    text = models.TextField('Text', max_length=2000, null=True, blank=True)
    text2 = models.TextField('Text2', max_length=2000, null=True, blank=True)
    image = models.ImageField('Image', upload_to='media/', null=True, blank=True)
    cropping = ImageRatioField('image', '460x220')


class Advices(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    text = models.TextField(max_length=10000, null=True, blank=True)
    image = models.ImageField('Image', upload_to='media/', null=True, blank=True)
    cropping = ImageRatioField('image', '900x300')


class ForPatientBlog(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    text = models.TextField(max_length=10000, null=True, blank=True)