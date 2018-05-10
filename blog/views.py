from django.shortcuts import render,get_object_or_404
from blog.models import Mytext

# Create your views here.
def index(request):
    index_page = render(request,'index.html')
    return index_page

def me(request):
    me_page = render(request,"me.html")
    return me_page

def mywork(request):
    work_page = render(request,'mywork.html')
    return work_page



def blog(request):
    artical = Mytext.objects.all()
    return render(request,'blog.html',{'artical':artical})

def artical(request,id):
    artic = Mytext.objects.get(id = id)
    post = Mytext.objects.all()
    return render(request,'artical.html',{'artical':artic,'post':post})

def journey(request):
    return render(request,'journey.html')

