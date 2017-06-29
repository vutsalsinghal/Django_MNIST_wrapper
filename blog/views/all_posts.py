from django.shortcuts import render
from django.utils import timezone
from blog.models import	Post

def	page(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return	render(request,	'all_posts.html',	{'posts':posts})
