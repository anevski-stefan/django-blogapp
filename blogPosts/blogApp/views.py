from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect

from blogApp.models import BlogPost, PostComment, UserInfo

from blogApp.forms import AddPostForm, EditInfoForm, AdminEditForm


# Create your views here.

def Home(request):
    all_posts = BlogPost.objects.all()
    context = {"posts":all_posts}
    return render(request, 'home.html', context=context)

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('/posts')


def Delete(request, id):
    blog_post = BlogPost.objects.get(id=id)
    blog_post.delete()
    return redirect('/posts')

def Readmore(request, id):
    blog_post = BlogPost.objects.get(id=id)
    user = blog_post.author
    userinfo = UserInfo.objects.get(user = user)
    file = blog_post.file
    comments = PostComment.objects.filter(blog_post=blog_post)
    context = {"post":blog_post, "comments": comments, "userinfo":userinfo, 'file':file}
    return render(request, 'readmore.html', context=context)

def Comment(request, id):
    blog_post = BlogPost.objects.get(id=id)
    if request.method == 'POST':
        user = request.user
        content = request.POST['comment']
        comment = PostComment(author_post = user, content_comment = content, blog_post=blog_post)
        comment.save()
    comments = PostComment.objects.filter(blog_post=blog_post)
    context = {"post":blog_post, 'comments':comments}
    return render(request, 'readmore.html', context=context)


def UserProfileInfo(request, username):
    user = User.objects.get(username=username)
    cuser = UserInfo.objects.get(user=user)
    blog_posts = BlogPost.objects.filter(author=user)
    context = {"user": user, "cuser":cuser, 'posts':blog_posts}
    return render(request, 'userinfo.html', context=context)

def DeleteComment(request, postid, commentid):
    comment = PostComment.objects.get(id=commentid)
    post = BlogPost.objects.get(id=postid)
    comment.delete()
    return redirect('/posts')


def SearchPosts(request):
    if request.method == 'POST':
        query = request.POST['query']
        posts = BlogPost.objects.filter(title__contains=query)
        context = {'posts': posts}
        return render(request, 'home.html', context=context)
    else:
        return render(request, 'home.html',{})


def download_file(request, id):
    blog_post = BlogPost.objects.get(id=id)
    return FileResponse(blog_post.file, as_attachment=True)

def AddPost(request):
    if request.method == 'POST':
        form=AddPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            obj = form.instance
            return redirect('/posts/')
    else:
        form = AddPostForm()
    return render(request, 'addPost.html', {'form':form})

def EditInfoPage(request, username):
    user = User.objects.get(username=username)
    userinfo = UserInfo.objects.get(user=user)
    if request.method == 'POST':
        form = EditInfoForm(data=request.POST, files=request.FILES, instance=userinfo)
        form2 = AdminEditForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
        if form2.is_valid():
            form2.save()
            return redirect('home')
    else:
        user = User.objects.get(username=username)
        userinfo = UserInfo.objects.get(user=user)
        form = EditInfoForm(instance=userinfo)
        form2 = AdminEditForm(instance=user)
    return render(request, 'editInfo.html', {'form':form, 'form2':form2})

def changePhoto(request, username):
    user = User.objects.get(username = username)
    userinfo = UserInfo.objects.get(user=user)
    if request.method == 'POST':
        if request.FILES.get('image'):
            userinfo.image = request.FILES['image']
            userinfo.save()
            return redirect('home')
