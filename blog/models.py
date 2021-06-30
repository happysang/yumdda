from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    writer = models.CharField(max_length=10)
    date = models.DateTimeField()
    body = models.TextField(default="")
    image = models.ImageField(upload_to ="blog/", blank=True, null=True)
 
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:5]