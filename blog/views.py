# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import EmailPostForm
from django.core.mail import send_mail
from taggit.models import Tag

# Create your views here.
def post_list(request, tag_slug=None):
    object_list=Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)#3 posts in each page
    page = request.GET.get('page')
    try:
    	posts = paginator.page(page)
    except PageNotAnInteger:
    	#if page is not an integer deliver the first page
    	posts = paginator.page(1)
    except EmptyPage:
    	#if page is out of range deliver last page of results
    	posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page':page, 'posts':posts, 'tag':tag, 'active_blog': True})

def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post, slug=post,
		status='published',
		publish__year=year,
		publish__month=month,
		publish__day=day)
	return render(request, 'blog/post/detail.html', {'post':post, 'active_blog': True})


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    else:
        
        if request.user.is_authenticated():
            form = EmailPostForm(initial = {'email': request.user.email})
        else:
            form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent,  'active_blog': True})