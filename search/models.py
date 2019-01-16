from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                    self).get_queryset()\
                         .filter(status='published')

class Thesis(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, 
                unique_for_date='publish')
    abstract = models.TextField()
    authors = models.CharField(max_length=250)
    posted_by = models.ForeignKey(User,null=True,blank=True,
                on_delete=models.SET_NULL,
                related_name='posts')
    adviser = models.ForeignKey(User, null=True, blank=True,
            on_delete=models.SET_NULL,
            related_name='advisees')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                choices=STATUS_CHOICES,
                    default='draft')
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)
        verbose_name_plural = "Theses"

        
    def get_absolute_url(self):
        return reverse('search:thesis_detail',
                        args=[self.publish.year,
                              self.publish.month,
                              self.publish.day,
                              self.slug])
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Thesis,
                             on_delete=models.CASCADE,
                             related_name='comments')
    user = models.ForeignKey(User,null=True,blank=True,
                on_delete=models.SET_NULL,
                related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.post)    
