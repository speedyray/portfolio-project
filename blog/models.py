from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.title)

    def summary(self):
        return self.body[:300]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

