from django.contrib.auth.models import User
from django.db import models
class Maqola(models.Model):
    title = models.CharField(max_length=100)
    matn = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Rasm(models.Model):
    photo = models.FileField(upload_to='static/media/')
    maqola = models.ForeignKey(Maqola,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.maqola.title}'

class Comment(models.Model):
    comments = models.TextField()
    maqola = models.ForeignKey(Maqola, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user},({self.comments})"

class About(models.Model):
    sarlavha = models.CharField(max_length=300,blank=True)
    matn = models.TextField()
    rasm = models.FileField(blank=True,upload_to='static/media/')
    def __str__(self):
        return f"{self.sarlavha}, {self.matn}"
