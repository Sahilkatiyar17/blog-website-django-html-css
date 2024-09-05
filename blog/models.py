from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #this is basically the table for user which django have created using admin etc. and we will connect it to Posts using the foreign key.
from django.urls import reverse 
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    # date_posted=models.DateTimeField(auto_now_add=True)
    # here auto_now_add will always show the date and time of the post created
    # but here you won't be able to update it 
    # date_posted=models.DateTimeField(auto_now=True)
    # here it will show the current time and date and you can update
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE) # if user gets deleted , it will delete the post releated to it
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})    

