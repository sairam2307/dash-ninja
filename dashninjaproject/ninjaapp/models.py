from django.db import models
import uuid
from django.utils import timezone
import datetime
from django.utils.text import slugify



# Create your models here.

class Category(models.Model):
    '''
        all main categories
    '''
    name = models.CharField(max_length=200, unique=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=90,blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = str(self.name)
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'categories'


class Items(models.Model):
    '''
        items related to categories
    '''

    name = models.CharField(max_length=200, unique=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=90,blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = str(self.name)
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'items'


class Footer(models.Model):
    '''
        items related to categories
    '''

    name = models.CharField(max_length=200, unique=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=90,blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = str(self.name)
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'footer'


class Company(models.Model):
    '''
        items related to categories
    '''

    name = models.CharField(max_length=200, unique=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=90,blank=True, null=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = str(self.name)
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'company'       