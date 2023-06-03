"""blogPosts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blogApp.views import Login, Home, Logout, Delete, Readmore, Comment, UserProfileInfo, DeleteComment,SearchPosts, download_file, AddPost, EditInfoPage, changePhoto


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login, name='login'),
    path('posts/', Home, name='home'),
    path('posts', Home, name='home'),
    path('logout/', Logout, name='logout'),
    path('posts/<int:id>/delete/', Delete, name='Delete'),
    path('posts/<int:id>/', Readmore, name='Readmore'),
    path('posts/<int:id>/comment/', Comment, name='Comment'),
    path('posts/profile/<username>', UserProfileInfo, name='UserProfileInfo'),
    path('posts/<int:postid>/comment/<int:commentid>/', DeleteComment, name='DeleteComment'),
    path('posts/search', SearchPosts, name='searchposts'),
    path('download/<int:id>/', download_file, name='download_file'),
    path('posts/add/', AddPost, name='AddPost'),
    path('posts/profile/<username>/edit', EditInfoPage, name='EditInfoPage'),
    path('posts/profile/<username>/profilephoto', changePhoto, name='changePhoto')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
