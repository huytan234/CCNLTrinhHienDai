from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField



class User(AbstractUser):
    avatar = CloudinaryField(null=True)



class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True



class Category(BaseModel):
    objects = None
    name = models.CharField(max_length=255, unique=True)
    icon = models.CharField(max_length=20, default='tag')

    def __str__(self):
        return self.name

class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name




class Course(BaseModel):
    objects = None
    name = models.CharField(max_length=255)
    description = RichTextField()
    # image = models.ImageField(upload_to='course/%Y/%m/')
    image = CloudinaryField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name



class Lesson(BaseModel):
    objects = None
    subject = models.CharField(max_length=255)
    content = RichTextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = CloudinaryField()
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return self.subject

class Interaction(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        abstract = True

class Comment(Interaction):
    objects = None
    content = models.CharField(max_length=255)



class Like(Interaction):
    objects = None

    class Meta:
        unique_together = ('lesson', 'user')





