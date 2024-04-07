#makemigrations و migrate
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
class post(models.Model):
    image=models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    test=models.CharField(max_length=255)
    content=models.TextField()
    tags = TaggableManager()
    category=models.ManyToManyField(Category)
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    login_require=models.BooleanField(default=False)
    publish_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{} {}'.format(self.test,self.id)

    class Meta:
        ordering=['created_date']
    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})
    

class comment(models.Model):
    post=models.ForeignKey(post,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject = models.CharField(max_length=255)
    message=models.TextField()
    approwed=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['created_date']
    def __str__(self):
        return self.name