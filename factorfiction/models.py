from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone

# An entity representing a news article.
# Has a many-to-one relationship with users
# (Many articles are written by each user)
class Page(models.Model):
	title = models.CharField(max_length=128)
	content = models.TextField(default=" ")
	postedBy = models.CharField(max_length=128,default="admin")
	url = models.CharField(max_length=250)
	articleImage = models.CharField(max_length=128)
	views = models.IntegerField(default=0)
	created_date = models.DateTimeField(default=timezone.now)
	facts = models.IntegerField(default=0)
	fictions = models.IntegerField(default=0)
	totalVotes = models.IntegerField(default=0)

	slug = models.SlugField()
	def save(self, *args, **kwargs):
		self.totalVotes = (self.facts + self.fictions)
		self.slug = slugify(self.title)
		super(Page, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'pages'

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

# An entity representing a comment on news
# article.
# Has a many-to-one relationship with pages
# (Many comments are made on each article)
class Comment(models.Model):
	page = models.ForeignKey(Page, related_name='comments')
	postedBy = models.ForeignKey(User, on_delete=models.PROTECT)
	text = models.CharField(max_length = 2000)
	created_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return (self.postedBy.username + " - " + str(self.created_date))

	def __unicode__(self):
		return (self.postedBy.username + " - " + str(self.created_date))
		

# An entity representing a news story for
# the fact or fiction game.
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

# An entity representing a user's profile.
# Has a one-to-one relationship with users
# (Each profile belongs to one user)
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	# The additional attributes we wish to include.
	name = models.CharField(max_length=128)
	age = models.IntegerField(default=0)
	picture = models.ImageField(upload_to='profile_images',default = "profile_images/default.png", blank=True)
	website = models.URLField(blank=True)
	location = models.CharField(max_length=128, default='')
	bio = models.CharField(max_length=1500, default='')

	
	# Override the __unicode__() method to return out something meaningful!
	def __str__(self):
		return self.user.username
	def __unicode__(self):
		return self.user.username

# A temporary model used to store info when
# a user is editing their profile.
class UpdateProfile(models.Model):
	user = models.OneToOneField(User)
	# The additional attributes we wish to include.
	name = models.CharField(max_length=128)
	age = models.IntegerField(default=0)
	picture = models.ImageField(upload_to='profile_images',default = "profile_images/default.png", blank=True)
	website = models.URLField(blank=True)
	location = models.CharField(max_length=128, default='')
	bio = models.CharField(max_length=1500, default='')

	
	# Override the __unicode__() method to return out something meaningful!
	def __str__(self):
		return self.user.username
	def __unicode__(self):
		return self.user.username

# A middle model used to implement a many-
# to-many relationship between Users and
# Pages. This keeps track of which pages
# the user has voted on so that they may
# only vote on each page once.
class UserVotes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	page = models.ForeignKey(Page, on_delete=models.CASCADE)