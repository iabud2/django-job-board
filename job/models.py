from django.db import models
from django.utils.text import slugify

# Create your models here.

JOB_TYPE = ( 
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time')
)



def image_upload(instance, filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id, extension)


class Job(models.Model):
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)

    slug = models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)



    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__ (self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply', on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    Email = models.EmailField(max_length=50)
    website = models.URLField(max_length=100)
    cv = models.FileField(upload_to='apply/')
    coverletter = models.TextField(max_length=1500)

    def __str__(self):
        return self.name
