from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Page(models.Model):
    title = models.CharField(max_length=128)
    postedBy = models.CharField(max_length=128,default="admin")
    url = models.URLField()
    views = models.IntegerField(default=0)
    facts = models.IntegerField(default=0)
    fictions = models.IntegerField(default=0)

    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'pages'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.title
		
class GameArticle(models.Model):
	title = models.CharField(max_length=128)
	description = models.CharField(max_length=5000)
	answer = models.CharField(max_length=7)
	fact = models.IntegerField(default=0)
	fiction = models.IntegerField(default=0)
	picture = models.CharField(max_length=128)
	
	def save(self, *args, **kwargs):
		super(GameArticle, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'GameArticles'

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    name = models.CharField(max_length=128)
    age = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username
    def __unicode__(self):
        return self.title