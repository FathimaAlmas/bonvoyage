from django.http import HttpResponseForbidden
from django.shortcuts import render,redirect,get_object_or_404
from .models import Bloggs
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'base/index.html')

def aboutus(request):
    return render(request,'base/aboutus.html')

def contactus(request):
    return render(request,'base/contactus.html')


def blog(request):
    bloggs=Bloggs.objects.all()
    return render(request,'base/blog.html',{'bloggs':bloggs})

@login_required
def add_blog(request):
    if request.method == 'POST':
        name = request.POST.get('blog_name')
        img = request.FILES.get('blog_img')
        date = request.POST.get('blog_date')
        description = request.POST.get('blog_description')
        head1 = request.POST.get('blog_head1')
        para1 = request.POST.get('blog_para1')
        head3 = request.POST.get('blog_head3')
        para3 = request.POST.get('blog_para3')
        para4 = request.POST.get('blog_para4')
    
        user = request.user
        
        Bloggs.objects.create(
            name=name,
            img=img,
            date=date,
            description=description,
            head1=head1,
            para1=para1,
            head3=head3,
            para3=para3,
            para4=para4,
            user=user  
        )
        return redirect('blog')
    return render(request, 'base/add_blog.html')


def viewblog(request):
    
    bloggs = Bloggs.objects.filter(user=request.user)
    
    return render(request,'base/viewblog.html',{'bloggs':bloggs})

@login_required
def update_blog(request, blog_id):
    bloggs = get_object_or_404(Bloggs, id=blog_id)
    if request.user != bloggs.user:
        # Handle unauthorized access (e.g., show an error message or redirect)
        return HttpResponseForbidden("You are not authorized to edit this blog.")
    if request.method == 'POST':
        bloggs.name = request.POST.get('blog_name')
        bloggs.img=request.FILES.get('blog_img')
        bloggs.date=request.POST.get('blog_date')
        bloggs.description = request.POST.get('blog_description')
        bloggs.head1 = request.POST.get('blog_head1')
        bloggs.para1 = request.POST.get('blog_para1')
        bloggs.head3 = request.POST.get('blog_head3')
        bloggs.para3 = request.POST.get('blog_para3')
        bloggs.para4 = request.POST.get('blog_para4')
        bloggs.save()
        return redirect('blog')
    return render(request, 'base/updateblog.html', {'bloggs': bloggs})

@login_required
def delete_blog(request, blog_id):
    bloggs= get_object_or_404(Bloggs, id=blog_id)
    if request.user != bloggs.user:
             # Handle unauthorized access (e.g., show an error message or redirect)
        return HttpResponseForbidden("You are not authorized to delete this blog.")
    if request.method == 'POST':

        bloggs.delete()
        return redirect('blog')
    return render(request, 'base/blog.html', {'bloggs': bloggs})
   

from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment
from django.contrib.auth.decorators import login_required

@login_required
def comments_list(request):
    user_comments = Comment.objects.filter(user=request.user)
    return render(request, 'base/comments.html', {'user_comments': user_comments})


def create_comment(request):
    if request.method == 'POST':
        text = request.POST.get('comment_text') 
        Comment.objects.create(user=request.user, text=text)
       
        return redirect('create_comment')
    else:
        comments = Comment.objects.all()
        return render(request, 'base/create_comment.html', {'comments': comments})

@login_required
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.text = request.POST.get('comment_text')
        comment.save()
        return redirect('create_comment')
    return render(request, 'base/update_comment.html', {'comment': comment})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('comments_list')
    return render(request, 'base/comments.html', {'comment': comment})

# Create your views here.
