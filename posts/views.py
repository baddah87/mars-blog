# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def post_list(request):
    obj_list = Post.objects.all()#.order_by("-timestamp","-updated")

    paginator = Paginator(obj_list, 8) 
    page = request.GET.get('page')
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objs = paginator.page(paginator.num_pages)
    context = {


    "post_list" : objs,



    }
    return render(request, 'post_list.html', context)



def post_detail(request, post_id):
	obj = get_object_or_404(Post, id=post_id) 
	context= {
	"instance": obj,
	}


	return render(request, 'post_detail.html', context)

def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		messages.success(request, "You created an object!!")
		return redirect("posts:list")
	context ={
		"form" : form,
	}
	return render(request, 'post_create.html', context)


def post_update(request, post_id):
	post_object = get_object_or_404(Post, id=post_id)
	form = PostForm(request.POST or None,request.FILES or None, instance=post_object)
	if form.is_valid():
		form.save()
		messages.success(request, "Are you sure?")
		return redirect("posts:list")
	context ={
		"form" : form,
		"post_object": post_object,
	}
	return render(request, 'post_update.html', context)
def post_delete(request, post_id):
	obj= Post.objects.get(id=post_id).delete()
	messages.warning(request, "really???")
	return redirect("posts:list")





