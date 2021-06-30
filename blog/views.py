from django.core import paginator
from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import BlogForm
from django.core.paginator import Paginator

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def home(request):
    #blogs = Blog.objects.all()
    orderblogs = Blog.objects.order_by('-date')
    search = request.GET.get('search')
    if search == 'true':
        author = request.GET.get('writer')
        blogs = Blog.objects.filter(writer=author)
        return render(request, 'home.html',{'viewsblogs':orderblogs})

    paginator = Paginator(orderblogs, 5)
    page = request.GET.get('page') ##??
    blogs = paginator.get_page(page)
    return render (request, 'home.html', {'viewsblogs':blogs})

def detail(request,each_id):
    blog = get_object_or_404(Blog, pk = each_id) ##첫번째 매개변수는 어떤 클래스에서 객체를 가져올지, 두번째 메개변수는 앞의 클래스의 몇번째 객체인지를 결정
    return render (request, 'detail.html', {'viewsblog':blog})

def new (request):
    new_form = BlogForm()
    return render (request, 'new.html', {'viewsform':new_form})

def create (request):
    create_form = BlogForm(request.POST,request.FILES)
    if create_form.is_valid():
        create_blog = create_form.save(commit=False) #commit=False 인 이유는 date가 아직 입력되지 않았기 때문에 임시저장 하는 것임!
        create_blog.date = timezone.now()
        create_blog.save()
        return redirect ('urlnamedetail', create_blog.id)
    # else:
    #     return redirect ('urlnamehome')
    # new_blog = Blog()
    # new_blog.title = request.POST['htmltitle']
    # new_blog.writer = request.POST['htmlwriter']
    # new_blog.body = request.POST['htmlbody']
    # new_blog.date = timezone.now()
    # new_blog.image = request.FILES.get('htmlimage') ## .get을 추가하였다. [] 도 ()로 변경
    # new_blog.save()
    # return redirect ('urlnamedetail', new_blog.id) # redirect 일때만 url 이름을 쓰나..?

def edit (request,each_id):
    edit_blog = Blog.objects.get(id = each_id)
    return render (request, 'edit.html', {'viewseditblog':edit_blog})

def update (request,each_id):
    edit_blog = Blog.objects.get(id = each_id)
    edit_blog.title = request.POST['htmltitle']
    edit_blog.writer = request.POST['htmlwriter']
    edit_blog.body = request.POST['htmlbody']
    edit_blog.image = request.FILES['htmlimage']
    edit_blog.date = timezone.now()
    edit_blog.save()
    return redirect ('urlnamedetail', edit_blog.id)

def delete (requset, each_id):
    delete_blog = Blog.objects.get(id = each_id)
    delete_blog.delete()
    return redirect ('urlnamehome')