from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
	user_auth      = models.OneToOneField(User, primary_key =True, help_text="Uername should be unique")
	name           = models.CharField(max_length=50, verbose_name="Name")
	email          = models.EmailField(verbose_name="Email")
	password       = models.CharField(max_length=100, verbose_name="Password")
	activation_key = models.CharField(max_length=40, blank=True)
	key_expires    = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.user_auth.username

class Post(models.Model):
	author         = models.ForeignKey('UserProfile', related_name='post_userProfile')
	title          = models.CharField(max_length = 500)
	text           = models.TextField()
	created_date   = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True, default = timezone.now)
	slug           = models.SlugField(('slug'), max_length=60, blank=True)
	post_labels    = models.CharField(max_length=500, verbose_name="Petition Label")
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title