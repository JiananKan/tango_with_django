from django.db import models
import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True,default="")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    #date = models.DateTimeField('date published')
    
    class Meta:
        verbose_name_plural = 'Categories'
        #def createtime(self):
        #self.date = timezone.now()
    def __str__(self):
        return self.name
        #def was_published_recently(self):
        #now = timezone.now()
        #return now - datetime.timedelta(days=1) <= self.date <= now
        #def was_published_recently(self):
        #print (self.date)
        #print (self.name)
#return self.date >= timezone.now() - datetime.timedelta(days=1)
        #was_published_recently.admin_order_field = 'date'
        #was_published_recently.boolean = True
#was_published_recently.short_description = 'Published recently?'

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
