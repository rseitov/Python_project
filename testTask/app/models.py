from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

class Directory(models.Model):

    name = models.CharField(max_length=200,blank=True)
    short_description = models.CharField(max_length=200,blank=True)
    full_description = models.CharField(max_length=200, blank=True)
    version = models.CharField(max_length=200,unique=True,null=False)
    start_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Element_directory(models.Model):
    parent_id = models.ForeignKey(Directory, on_delete=models.CASCADE)
    kod_el = models.CharField(unique=True,null=False,max_length=100)
    value = models.CharField(null=False,max_length=200)

    def __str__(self):
        return self.value




