from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    content = models.TextField(null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created', '-updated']
    
    def __str__(self):
        return self.title

class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'summary', 'content']