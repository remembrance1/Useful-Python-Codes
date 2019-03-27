from django.db import models

class Job(models.Model): #create a new class in py called Job
    image = models.ImageField(upload_to = 'images/') #image uploaded shld be sent to this folder
    summary = models.CharField(max_length = 200)
