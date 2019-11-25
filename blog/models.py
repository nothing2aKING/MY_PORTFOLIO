from django.db import models

# Create your models here.

class Blog(models.Model):
    #Blog Objects
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    #return 10 characters from the body 
    def summary(self):
        return self.body[:20]

    def pub_date_nice(self):
        return self.pub_date.strftime('%b %e %Y')
