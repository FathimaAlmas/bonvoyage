from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"Review by {self.user.username}"
    
class Bloggs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.TextField()
    date=models.DateField()
    img=models.ImageField(upload_to='bloggs')
    description=models.TextField()
    head1=models.TextField()
    para1=models.TextField()
    head3=models.TextField()
    para3=models.TextField()
    para4=models.TextField()

    
    


    