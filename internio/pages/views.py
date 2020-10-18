from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Contact, Job, BlogPost
from .forms import ContactForm, JobForm, EmailSubscriptionForm
# Create your views here.




def IndexPage(request):
    blog_posts = BlogPost.objects.filter(status=1).order_by('-created_on')[:4]
    context_object_name = {'blog_posts':blog_posts}
    return render(request, 'pages/index.html', context_object_name)


def AboutPage(request):
    context_object_name = {'title':'About'}
    return render(request, 'pages/about.html', context_object_name)

def ContactPage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Message Sent Successfully')
            return redirect('homepage')
    else:
        form = ContactForm()
        return render(request, 'pages/contact.html', {'title':'Contact', 'form':form})

def BlogPage(request):
    blog_posts = BlogPost.objects.filter(status=1).order_by('-created_on')
    context_object_name = {'title':'Blog', 'blog_posts':blog_posts}
    return render(request, 'pages/blog.html', context_object_name)
# class BlogPostList(generic.ListView):
#     query_set = BlogPost.objects.filter(status=1).order_by('-created_on')
#     template_name = 'pages/blog.html'

# class SingleBlogPost(generic.DetailView):
#     model = BlogPost
#     template_name = 'pages/blog-single.html'

def SingleBlogPost(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    recents = BlogPost.objects.filter(status=1).order_by('-created_on')[:3]

    return render(request, 'pages/blog-single.html', {'blog_post':blog_post, 'recents': recents})

def NewPost(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Job Created Successfully', extra_tags='alert alert-success')
            return redirect('newpost')
    else:
        form = JobForm()
        return render(request, 'pages/newpost.html', {'title':'Post a Job', 'form':form})
def EmailSubscribe(request):
    if request.method == "POST":
        form = EmailSubscriptionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Subscription Added Successfully!')
            return redirect('homepage')
    else:
        form = EmailSubscriptionForm()
        return render(request, 'pages/master.html',{'f':form})


