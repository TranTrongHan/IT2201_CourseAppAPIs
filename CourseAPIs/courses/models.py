
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Course(BaseModel):
    subject = models.CharField(max_length=100,unique=True)
    description = models.TextField(max_length=255,null=True)
    image = models.ImageField(upload_to='courses/%Y/%m',null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.subject

class Lesson(BaseModel):
    subject = models.CharField(max_length=100, unique=True)
    content = RichTextField()
    image = models.ImageField(upload_to='lessons/%Y/%m', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    def __str__(self):
        return self.subject

class Tag(BaseModel):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name