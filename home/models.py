from functools import update_wrapper
from django.db import models

# Create your models here.
# Home section
class Home(models.Model):
    name = models.CharField(max_length=100)
    greeting_1= models.CharField(max_length=5)
    geeting_2 = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='pitcure')
    updated =models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.name


# About section

class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=20)
    description =models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='profile/')

    updated =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career

class profile(models.Model):
    about = models.ForeignKey(About,
                                on_delete=models.CASCADE)
    social_name =models.CharField(max_length=10)
    link = models.URLField(max_length=200)


# skills section

class category(models.Model):
    Name = models.CharField(max_length=20)
    updated =models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Skills"
        verbose_name_plural = "Skills"
    
    def __str__(self):
         return self.Name

class Skills(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    skill_name =models.CharField(max_length=20)


# portfolio  section

class portfolio(models.Model):
    image =models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'portfolio {self.id}'

    