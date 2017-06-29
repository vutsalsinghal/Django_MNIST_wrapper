"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import index, connect, logout, create_user, register_confirm, all_posts, post_detail, mnist

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', index.page, name="index"),
	url(r'^connect$', connect.page, name="connect"),
	url(r'^logout$', logout.page, name="logout"),
	url(r'^create_user$', create_user.page, name="create_user"),
	url(r'^accounts/confirm/(?P<activation_key>\w+)/', register_confirm.page, name='email_confirm'),

	#..................................................................................................................#
	url(r'^all_posts$', all_posts.page, name="all_posts"),
	url(r'^post/(?P<slug>[-\w]+)/$', post_detail.page, name="post_detail"),
	url(r'^mnist$', mnist.page, name="mnist"),
]