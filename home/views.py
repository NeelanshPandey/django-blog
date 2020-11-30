from django.shortcuts import render, HttpResponseRedirect, get_object_or_404,redirect
from django.contrib import messages


from .models import Blogs, CommentBlog,HelpMessage
from datetime import datetime

# Create your views here.


def index(request):
    # for Blog Entry
    if request.method == "POST":
        title = request.POST.get('blogTitle')
        author = request.POST.get('blogAuthor')
        content = request.POST.get('blogContent')
        blog = Blogs(blogTitle=title, blogAuthor=author,
                     blogContent=content, time=datetime.today())
        blog.save()
        messages.success(
            request, 'Congratulations: Your Blog Have been added in blogry.')
        return HttpResponseRedirect('/')
    q = request.GET.get('searchQuery', None)
    if q == None or q == "":
        blogs = Blogs.objects.all()[::-1]
    else:
        blogs = Blogs.objects.filter(blogTitle__contains=q)
    return render(request, 'home/index.html', {'blogs': blogs})


def createBlog(request):

    return render(request, 'home/createBlog.html')


def details(request, id=None):
    data = Blogs.objects.get(id=id)
    if request.method == 'POST':
        commentName = request.POST.get('commentName')
        commentText = request.POST.get('commentText')
        comment = CommentBlog(commentName=commentName, commentText=commentText, blog=data)
        comment.save()
        return redirect("/details/{}/".format(data.id))

    blog = get_object_or_404(Blogs, id=id)
    comments = CommentBlog.objects.filter(blog=data)
    return render(request, 'home/details.html', {'blog': blog, 'comments': comments,'data':data})

def about(request):
    return render(request, 'home/about.html')

def faqs(request):
    return render(request,'home/faqs.html')

def help(request):
    if request.method=="POST":
        helpName=request.POST.get('helpName')
        helpText=request.POST.get('helpText')
        helpmsg=HelpMessage(helpName=helpName,helpText=helpText)
        helpmsg.save()
        messages.success(
            request, 'Your Message / Question has been sent')
        return redirect("/help")
    return render(request,'home/help.html')
