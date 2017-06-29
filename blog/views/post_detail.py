from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from blog.models import Post, UserProfile
from django.contrib.auth.decorators import login_required
from django import forms
from django.http import HttpResponse

@login_required
def page(request, slug):
    post     = get_object_or_404(Post, slug=slug)
    user_obj = UserProfile.objects.get(name=request.user)
    if post.author == user_obj:
        user_edit = True
    else:
        user_edit = False
    if  request.method == "POST":
        form = CommentForm(request.POST)
        if  form.is_valid():
            author = form.cleaned_data['author']
            text   = form.cleaned_data['text']
            
            new_comment = Comment(author=author, text=text, post=post)
            new_comment.save()
            return redirect('/post/' + str(slug))
        else:
            return HttpResponse('Comment form is empty and/or invalid')
    else:
        form =  CommentForm()
        return render(request, 'post_detail.html', {'post':post, 'user_edit':user_edit, 'form': form})

class CommentForm(forms.Form):
    author = forms.CharField(label="Author", max_length=500, widget=forms.TextInput(attrs={'placeholder':'Can Be Anonymous'}))
    text   = forms.CharField(label="Comment", widget=forms.Textarea(attrs={'placeholder':'Your Opinion', 'class':'materialize-textarea'}))