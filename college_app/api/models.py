from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100, )
    def __str__(self):
        return self.name

class Post(models.Model):
    posterName = models.CharField(max_length=100)
    original = models.IntegerField()
    wish = models.IntegerField()
    subjects = models.ManyToManyField(Subject)
    date = models.DateTimeField(auto_now_add=True)
    acceptorName = models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return self.posterName
    